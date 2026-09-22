from datetime import datetime, timezone
from decimal import Decimal

from .extensions import db


def utcnow():
    return datetime.now(timezone.utc)


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(160), nullable=False)
    email = db.Column(db.String(254), nullable=True, index=True)
    phone = db.Column(db.String(40), nullable=False, index=True)
    document_type = db.Column(db.String(20), nullable=True)
    document_number = db.Column(db.String(30), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)

    addresses = db.relationship("Address", back_populates="customer", cascade="all, delete-orphan")
    orders = db.relationship("Order", back_populates="customer")


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    label = db.Column(db.String(40), nullable=False, default="principal")
    address_line = db.Column(db.String(240), nullable=False)
    district = db.Column(db.String(100), nullable=True)
    province = db.Column(db.String(100), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    reference = db.Column(db.String(240), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)

    customer = db.relationship("Customer", back_populates="addresses")
    orders = db.relationship("Order", back_populates="shipping_address")


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), nullable=False, unique=True, index=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False, index=True)
    shipping_address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=True)
    status = db.Column(db.String(32), nullable=False, default="pending_confirmation", index=True)
    payment_method = db.Column(db.String(32), nullable=False, default="pending")
    payment_status = db.Column(db.String(32), nullable=False, default="pending")
    fulfillment_mode = db.Column(db.String(32), nullable=False, default="manual")
    currency = db.Column(db.String(3), nullable=False, default="PEN")
    subtotal = db.Column(db.Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    shipping_cost = db.Column(db.Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    discount = db.Column(db.Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    total = db.Column(db.Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    customer_note = db.Column(db.Text, nullable=True)
    provider_reference = db.Column(db.String(120), nullable=True)
    tracking_code = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)

    customer = db.relationship("Customer", back_populates="orders")
    shipping_address = db.relationship("Address", back_populates="orders")
    items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    events = db.relationship("OrderEvent", back_populates="order", cascade="all, delete-orphan", order_by="OrderEvent.created_at")


class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = db.Column(db.Integer, nullable=True)
    product_slug = db.Column(db.String(160), nullable=False)
    product_name = db.Column(db.String(240), nullable=False)
    category = db.Column(db.String(40), nullable=True)
    unit_price = db.Column(db.Numeric(12, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    line_total = db.Column(db.Numeric(12, 2), nullable=False)
    product_snapshot = db.Column(db.JSON, nullable=True)

    order = db.relationship("Order", back_populates="items")


class OrderEvent(db.Model):
    __tablename__ = "order_events"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    from_status = db.Column(db.String(32), nullable=True)
    to_status = db.Column(db.String(32), nullable=False)
    note = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)

    order = db.relationship("Order", back_populates="events")
