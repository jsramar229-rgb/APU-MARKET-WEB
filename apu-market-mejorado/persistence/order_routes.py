from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .models import Order
from .order_service import create_order, change_order_status

orders_bp = Blueprint("orders", __name__, url_prefix="/api/orders")


def product_lookup_from_catalog(slug):
    # Ajusta este import al módulo de catálogo de tu proyecto.
    from catalogo import por_slug
    return por_slug(slug)


@orders_bp.post("")
def create_order_endpoint():
    payload = request.get_json(silent=True) or {}
    try:
        order = create_order(
            customer_data=payload.get("customer", {}),
            address_data=payload.get("address", {}),
            cart_items=payload.get("items", []),
            payment_method=payload.get("payment_method", ""),
            fulfillment_mode=payload.get("fulfillment_mode", "manual"),
            shipping_cost=payload.get("shipping_cost", 0),
            discount=payload.get("discount", 0),
            note=payload.get("note"),
            product_lookup=product_lookup_from_catalog,
        )
    except (ValueError, TypeError, KeyError) as exc:
        return jsonify({"error": str(exc)}), 400
    except SQLAlchemyError:
        from .extensions import db
        db.session.rollback()
        return jsonify({"error": "No se pudo guardar el pedido"}), 500

    return jsonify({
        "id": order.public_id,
        "status": order.status,
        "payment_status": order.payment_status,
        "total": str(order.total),
        "currency": order.currency,
    }), 201


@orders_bp.get("/<public_id>")
def get_order_endpoint(public_id):
    order = Order.query.filter_by(public_id=public_id).first_or_404()
    return jsonify({
        "id": order.public_id,
        "status": order.status,
        "payment_method": order.payment_method,
        "payment_status": order.payment_status,
        "tracking_code": order.tracking_code,
        "total": str(order.total),
        "currency": order.currency,
        "created_at": order.created_at.isoformat(),
        "items": [
            {
                "slug": item.product_slug,
                "name": item.product_name,
                "quantity": item.quantity,
                "unit_price": str(item.unit_price),
                "line_total": str(item.line_total),
            }
            for item in order.items
        ],
    })


@orders_bp.post("/<public_id>/status")
def update_order_status_endpoint(public_id):
    # Proteger esta ruta con autenticación de administrador antes de producción.
    payload = request.get_json(silent=True) or {}
    new_status = str(payload.get("status", "")).strip()
    note = str(payload.get("note", "")).strip() or None
    order = Order.query.filter_by(public_id=public_id).first_or_404()
    change_order_status(order, new_status, note)
    return jsonify({"id": order.public_id, "status": order.status})
