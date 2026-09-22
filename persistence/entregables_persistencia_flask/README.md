# Persistencia de pedidos y clientes para APU Market

Este kit agrega una capa persistente a la tienda Flask existente sin reemplazar el catálogo ni las plantillas actuales. Usa Flask-SQLAlchemy, Flask-Migrate y PostgreSQL. La estructura guarda clientes, direcciones, pedidos, líneas de pedido y eventos de estado.

## Estructura

```text
persistence/
  __init__.py
  extensions.py
  models.py
  order_service.py
  order_routes.py
  persistence_setup.py
requirements-persistencia.txt
render.yaml
```

Copia los archivos Python dentro de una carpeta llamada `persistence/` en la raíz de la aplicación. El `render.yaml` debe copiarse a la raíz del repositorio, ajustando `rootDir` si Render ya está configurado desde `apu-market-mejorado/`.

## Integración mínima en `app.py`

Añade después de crear Flask:

```python
from persistence.persistence_setup import configure_persistence
from persistence.order_routes import orders_bp

app = Flask(__name__)
configure_persistence(app)
app.register_blueprint(orders_bp)

@app.get("/health")
def health():
    return {"status": "ok"}, 200
```

Si tu repositorio mantiene `app.py` dentro de `apu-market-mejorado/`, coloca el paquete `persistence/` en esa misma carpeta o ajusta el `PYTHONPATH` para que Python pueda importarlo.

## Dependencias

Fusiona `requirements-persistencia.txt` con tu `requirements.txt` actual:

```text
Flask==3.0.3
gunicorn==22.0.0
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.7
psycopg[binary]==3.2.3
```

## Variables de entorno

En Render debes crear `DATABASE_URL` apuntando a PostgreSQL. Nunca escribas la contraseña en GitHub. El código convierte automáticamente los formatos `postgres://` y `postgresql://` al dialecto compatible con Psycopg 3.

## Migraciones locales

Desde la carpeta donde está `app.py`:

```bash
export FLASK_APP=app.py
flask db init
flask db migrate -m "crear clientes pedidos y estados"
flask db upgrade
```

Revisa la migración generada antes de subirla. En Render, ejecuta `flask db upgrade` como **Pre-Deploy Command** o como un paso controlado de despliegue. No uses `db.create_all()` en cada arranque: las migraciones deben ser la fuente de verdad del esquema.

## Payload para crear un pedido

La ruta `POST /api/orders` espera JSON como este:

```json
{
  "customer": {
    "full_name": "Nombre del cliente",
    "email": "cliente@example.com",
    "phone": "+51 999 999 999"
  },
  "address": {
    "address_line": "Av. Ejemplo 123",
    "district": "Miraflores",
    "province": "Lima",
    "department": "Lima",
    "reference": "Cerca del parque"
  },
  "items": [
    {"slug": "llavero-3d-personalizado", "quantity": 1}
  ],
  "payment_method": "yape-plin",
  "fulfillment_mode": "personalizado",
  "shipping_cost": 10,
  "discount": 0,
  "note": "Solicito confirmación del diseño antes de producir"
}
```

El servidor vuelve a consultar el catálogo por `slug`; no debe confiar en el precio enviado por el navegador. Cada `OrderItem` guarda una copia del nombre, precio, foto y categoría para conservar el comprobante histórico aunque el catálogo cambie.

## Estados sugeridos

```text
pending_confirmation -> confirmed -> paid -> preparing -> shipped -> delivered
pending_confirmation -> cancelled
confirmed -> rejected
```

Para Hanan Pacha, `fulfillment_mode` puede ser `dropshipping`. Para Kay Pacha, `organico`. Para Ukhu Pacha, `personalizado`. El cambio de estado debe registrar un `OrderEvent` con fecha y nota.

## Seguridad antes de producción

La ruta de actualización de estado está intencionalmente marcada para protegerse con autenticación de administrador. No la publiques abierta. Añade CSRF para formularios de sesión, rate limiting para creación de pedidos, validación de correo y teléfono, logs sin datos sensibles y una política de retención de datos. Para pagos en línea, crea una ruta de webhook idempotente y verifica el estado en backend; nunca marques un pedido como pagado solo porque el navegador regresó de una pasarela.

## Render y persistencia

El archivo `render.yaml` es una referencia. Si usas el PostgreSQL gratuito de Render, recuerda que la documentación de Render indica que esa base expira después de 30 días. Para pedidos reales debes usar un plan persistente con copias de seguridad o una base administrada equivalente. El servicio web gratuito también se suspende tras 15 minutos sin tráfico y tarda alrededor de un minuto en despertar.

## Próxima integración de frontend

El carrito actual debe enviar los `slug` y cantidades a `POST /api/orders`, junto con los datos solicitados en un formulario de checkout. Después de crear el pedido, usa el `public_id` para generar el mensaje de WhatsApp y mostrar al cliente una página de confirmación. No incluyas el número de documento si no es necesario para el pedido; solicítalo únicamente cuando sea requerido para emitir el comprobante.
