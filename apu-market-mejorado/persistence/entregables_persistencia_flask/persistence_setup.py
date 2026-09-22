import os

from flask import Flask

from .extensions import db, migrate


def configure_persistence(app: Flask) -> None:
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL no está configurada")

    # Render puede entregar postgres://; SQLAlchemy moderno requiere postgresql://.
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)

    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ENGINE_OPTIONS={
            "pool_pre_ping": True,
            "pool_recycle": 300,
        },
    )
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos después de vincular la extensión para que Alembic los detecte.
    from .models import Address, Customer, Order, OrderEvent, OrderItem  # noqa: F401
