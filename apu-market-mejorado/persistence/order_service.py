from decimal import Decimal, InvalidOperation
from uuid import uuid4

from .extensions import db
from .models import Address, Customer, Order, OrderEvent, OrderItem


ALLOWED_PAYMENT_METHODS = {"yape-plin", "transferencia", "contra-entrega", "mercado-pago"}
ALLOWED_FULFILLMENT_MODES = {"manual", "dropshipping", "personalizado", "organico"}


def money(value):
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError("Monto inválido") from exc
    if amount < 0:
        raise ValueError("El monto no puede ser negativo")
    return amount.quantize(Decimal("0.01"))


def required_text(data, key, max_length):
    value = str(data.get(key, "")).strip()
    if not value or len(value) > max_length:
        raise ValueError(f"Campo inválido: {key}")
    return value


def get_or_create_customer(customer_data):
    full_name = required_text(customer_data, "full_name", 160)
    phone = required_text(customer_data, "phone", 40)
    email = str(customer_data.get("email", "")).strip() or None
    if email and len(email) > 254:
        raise ValueError("Correo inválido")

    customer = None
    if email:
        customer = Customer.query.filter_by(email=email).first()
    if customer is None:
        customer = Customer.query.filter_by(phone=phone).first()
    if customer is None:
        customer = Customer(full_name=full_name, email=email, phone=phone)
        db.session.add(customer)
    else:
        customer.full_name = full_name
        customer.email = email or customer.email
        customer.phone = phone
    return customer


def get_or_create_address(customer, address_data):
    address_line = required_text(address_data, "address_line", 240)
    district = str(address_data.get("district", "")).strip() or None
    province = str(address_data.get("province", "")).strip() or None
    department = str(address_data.get("department", "")).strip() or None
    reference = str(address_data.get("reference", "")).strip() or None

    address = Address(
        customer=customer,
        label="principal",
        address_line=address_line,
        district=district,
        province=province,
        department=department,
        reference=reference,
    )
    db.session.add(address)
    return address


def create_order(*, customer_data, address_data, cart_items, payment_method, fulfillment_mode="manual", shipping_cost=0, discount=0, note=None, product_lookup):
    if payment_method not in ALLOWED_PAYMENT_METHODS:
        raise ValueError("Método de pago no disponible")
    if fulfillment_mode not in ALLOWED_FULFILLMENT_MODES:
        raise ValueError("Modalidad de despacho no disponible")
    if not cart_items:
        raise ValueError("El carrito está vacío")

    customer = get_or_create_customer(customer_data)
    address = get_or_create_address(customer, address_data)
    order = Order(
        public_id=str(uuid4()),
        customer=customer,
        shipping_address=address,
        status="pending_confirmation",
        payment_method=payment_method,
        payment_status="pending",
        fulfillment_mode=fulfillment_mode,
        customer_note=(str(note).strip()[:2000] if note else None),
    )
    db.session.add(order)

    subtotal = Decimal("0.00")
    for raw_item in cart_items:
        slug = required_text(raw_item, "slug", 160)
        quantity = int(raw_item.get("quantity", 0))
        if quantity < 1 or quantity > 99:
            raise ValueError("Cantidad inválida")
        product = product_lookup(slug)
        if not product:
            raise ValueError(f"Producto no disponible: {slug}")
        unit_price = money(product["precio"])
        line_total = (unit_price * quantity).quantize(Decimal("0.01"))
        subtotal += line_total
        item = OrderItem(
            order=order,
            product_id=product.get("id"),
            product_slug=product["slug"],
            product_name=product["nombre"],
            category=product.get("mundo"),
            unit_price=unit_price,
            quantity=quantity,
            line_total=line_total,
            product_snapshot={
                "nombre": product.get("nombre"),
                "slug": product.get("slug"),
                "foto": product.get("foto"),
                "mundo": product.get("mundo"),
                "precio_catalogo": str(product.get("precio")),
            },
        )
        db.session.add(item)

    order.subtotal = subtotal
    order.shipping_cost = money(shipping_cost)
    order.discount = money(discount)
    order.total = max(Decimal("0.00"), subtotal + order.shipping_cost - order.discount)
    db.session.add(OrderEvent(order=order, to_status="pending_confirmation", note="Pedido creado desde la tienda"))
    db.session.commit()
    return order


def change_order_status(order, new_status, note=None):
    old_status = order.status
    if old_status == new_status:
        return order
    order.status = new_status
    db.session.add(OrderEvent(order=order, from_status=old_status, to_status=new_status, note=note))
    db.session.commit()
    return order
