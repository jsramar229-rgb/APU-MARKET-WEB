# -*- coding: utf-8 -*-
"""
APU MARKET — Kimsa Pacha Qhatu
E-commerce de APU 3D SOLUCIONES INTEGRALES S.A.C.

Este archivo tiene la CONFIGURACIÓN y las RUTAS.
El catálogo de productos vive aparte, en catalogo.py

v1 sin base de datos: los pedidos salen por WhatsApp. Cuando haga falta control
de stock e historial de pedidos, se migra a Postgres.
"""

from flask import Flask, render_template, request, abort

from catalogo import PRODUCTOS

app = Flask(__name__)

# ---------------------------------------------------------------------------
# CONFIGURACIÓN — lo único que hay que tocar para salir a producción
# ---------------------------------------------------------------------------

EMPRESA = {
    "razon_social": "APU 3D SOLUCIONES INTEGRALES S.A.C.",
    "nombre_comercial": "APU Market",
    "ruc": "REEMPLAZAR-CON-RUC",             # <-- pendiente
    "whatsapp": "51991897256",                # <-- pendiente: real, sin + ni espacios
    "whatsapp_visible": "+51 991 897 256",    # <-- pendiente
    "correo": "contacto@apumarket.net",       # <-- pendiente: crear en Hostinger
    # Por criterio de privacidad no se publica la dirección exacta.
    "zona_atencion": "Lima, Perú — atención virtual y presencial a convenir",
    "horario": "Lunes a sábado, 9:00 a 19:00",
}

# Métodos visibles antes de publicar. Sustituye los datos marcados por los reales.
# El checkout actual es asistido por WhatsApp: aquí el cliente elige su preferencia
# y el equipo confirma los datos finales antes de cobrar.
PAGOS = [
    {
        "id": "yape-plin",
        "nombre": "Yape o Plin",
        "detalle": "Pago móvil — confirma el número por WhatsApp",
        "icono": "movil",
    },
    {
        "id": "transferencia",
        "nombre": "Transferencia bancaria",
        "detalle": "Te enviamos los datos de la cuenta al confirmar",
        "icono": "banco",
    },
    {
        "id": "contra-entrega",
        "nombre": "Contra entrega",
        "detalle": "Disponible según distrito y tipo de producto",
        "icono": "entrega",
    },
]

# Slot de campaña reutilizable.
CAMPANA = {
    # True enciende: barra superior, item del menu, franja en la portada
    # y la ruta /kusi-navidad.
    # Apagar (False) hasta fines de octubre si el sitio ya esta publicado.
    "activa": True,
    "slug": "kusi-navidad",
    "nombre": "Kusi Navidad 2026",
    "quechua": "Kusi — alegría",
    "lema": "La alegría navideña con raíz andina",
    "descripcion": (
        "Canastas que reúnen los tres mundos, retablos y nacimientos andinos de "
        "artesanos ayacuchanos, y piezas personalizadas en edición limitada."
    ),
    "barra": "Kusi Navidad 2026 — preventa abierta",
}

# ---------------------------------------------------------------------------
# LOS TRES MUNDOS
# ---------------------------------------------------------------------------

MUNDOS = {
    "kay": {
        "slug": "kay-pacha",
        "nombre": "Kay Pacha",
        "traduccion": "El mundo de aquí",
        "esencia": "lo terrenal",
        "rubro": "Orgánicos",
        "lema": "Lo que nace de la tierra",
        "descripcion": (
            "Productos orgánicos que crecen en el plano de aquí y ahora: miel, "
            "granos, hierbas y suplementos naturales de productores peruanos."
        ),
    },
    "hanan": {
        "slug": "hanan-pacha",
        "nombre": "Hanan Pacha",
        "traduccion": "El mundo de arriba",
        "esencia": "lo celestial",
        "rubro": "Importados",
        "lema": "Lo que viene de más allá del horizonte",
        "descripcion": (
            "Productos importados que llegan desde otros horizontes: tecnología, "
            "cuidado personal y accesorios seleccionados."
        ),
    },
    "ukhu": {
        "slug": "ukhu-pacha",
        "nombre": "Ukhu Pacha",
        "traduccion": "El mundo interior",
        "esencia": "las raíces",
        "rubro": "Personalizados",
        "lema": "Lo que nace desde adentro",
        "descripcion": (
            "Productos personalizados que se gestan en tu identidad y se "
            "materializan: impresión 3D, grabado, sublimación y bordado."
        ),
    },
}

# Origen por región — filtro que solo aplica a Kay Pacha, donde la procedencia
# peruana sí es información de valor para quien compra.
REGIONES = {
    "costa": "Costa",
    "sierra": "Sierra",
    "selva": "Selva",
}


# ---------------------------------------------------------------------------
# CONSULTAS AL CATÁLOGO
# ---------------------------------------------------------------------------

def productos_de(mundo=None, campana=None):
    """Filtra el catálogo. campana=None ignora el filtro de campaña."""
    items = PRODUCTOS
    if mundo:
        items = [p for p in items if p["mundo"] == mundo]
    if campana is True:
        items = [p for p in items if p.get("campana")]
    elif campana is False:
        items = [p for p in items if not p.get("campana")]
    return items


def por_slug(slug):
    return next((p for p in PRODUCTOS if p["slug"] == slug), None)


def destacados(n=6):
    """Dos productos de cada mundo para la portada."""
    sel = []
    for clave in MUNDOS:
        sel.extend(productos_de(clave, campana=False)[: n // 3])
    return sel


def relacionados(producto, n=4):
    """Otros productos del mismo mundo, excluyendo el actual."""
    hermanos = [p for p in productos_de(producto["mundo"]) if p["id"] != producto["id"]]
    return hermanos[:n]


@app.context_processor
def inyectar_globales():
    return {
        "empresa": EMPRESA,
        "pagos": PAGOS,
        "campana": CAMPANA,
        "mundos": MUNDOS,
        "anio": 2026,
    }


# ---------------------------------------------------------------------------
# RUTAS
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        destacados=destacados(6),
        productos_campana=productos_de(campana=True)[:3],
    )


@app.route("/producto/<slug>")
def producto(slug):
    p = por_slug(slug)
    if not p:
        abort(404)
    return render_template(
        "producto.html",
        p=p,
        mundo=MUNDOS[p["mundo"]],
        regiones=REGIONES,
        relacionados=relacionados(p),
    )


@app.route("/kusi-navidad")
def kusi_navidad():
    if not CAMPANA["activa"]:
        return render_template("campana_cerrada.html"), 404
    return render_template("campana.html", productos=productos_de(campana=True))


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/libro-de-reclamaciones")
def reclamaciones():
    return render_template("reclamaciones.html")


# Esta ruta va al final: al ser genérica, capturaría cualquier dirección de un
# solo tramo. Flask resuelve primero las rutas fijas de arriba.
@app.route("/<slug>")
def mundo(slug):
    clave = next((k for k, v in MUNDOS.items() if v["slug"] == slug), None)
    if not clave:
        abort(404)
    region = request.args.get("region")
    items = productos_de(clave, campana=False)
    if clave == "kay" and region in REGIONES:
        items = [p for p in items if p.get("region") == region]
    return render_template(
        "mundo.html",
        mundo=MUNDOS[clave],
        clave=clave,
        productos=items,
        regiones=REGIONES if clave == "kay" else None,
        region_activa=region,
    )


@app.errorhandler(404)
def no_encontrado(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
