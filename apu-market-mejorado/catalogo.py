# -*- coding: utf-8 -*-
"""
CATÁLOGO DE APU MARKET
======================

Este archivo es SOLO datos. Editarlo no toca la lógica de la aplicación.

CÓMO AGREGAR UN PRODUCTO
------------------------
Copia un bloque completo, pégalo al final de su sección y cambia los valores.
Reglas:

  id      número único, que no se repita con ningún otro
  slug    la dirección web del producto: minúsculas, sin tildes ni espacios,
          palabras separadas con guion.  ->  /producto/miel-de-abeja-andina
  mundo   "kay" | "hanan" | "ukhu"
  region  "costa" | "sierra" | "selva" | None   (solo se usa en Kay Pacha)
  foto    nombre del archivo dentro de static/img/productos/
          Mientras sea None se muestra el icono. Nada se rompe si falta la foto.
  icono   respaldo visual. Disponibles: miel, grano, raiz, botella, taza,
          audifonos, reloj, proyector, camara, tableta, parlante, llavero,
          polo, cuadro, funda, gorra, canasta, regalo, adorno, retablo,
          paneton, kimsa
  campana True solo si el producto pertenece a la campaña activa

Los bloques ficha / origen / envio son diccionarios libres: la clave es la
etiqueta que se ve en la página y el valor es el dato. Puedes poner las filas
que quieras, o dejarlos vacíos con {} si todavía no tienes la información.

IMPORTANTE
----------
Los textos de detalle de este archivo están casi todos VACÍOS a propósito.
No inventé descripciones, orígenes ni productores: publicar datos inventados
sobre el origen de un alimento es una afirmación falsa frente al consumidor.
Los tres productos marcados como EJEMPLO muestran el formato a seguir; los
demás esperan tus datos reales.
"""

PRODUCTOS = [

    # =====================================================================
    # KAY PACHA — Orgánicos
    # =====================================================================

    # ---- EJEMPLO COMPLETO: copia este bloque como plantilla ----
    {
        "id": 1,
        "slug": "miel-de-abeja-andina",
        "mundo": "kay",
        "region": "sierra",
        "nombre": "Miel de abeja andina 500 g",
        "precio": 35.0,
        "icono": "miel",
        "foto": None,                     # -> "miel-de-abeja-andina.webp"
        "etiqueta": "Orgánico",
        "desc": "Miel pura de valles andinos, cosechada artesanalmente y sin aditivos.",
        "descripcion_larga": (
            "REEMPLAZAR. Un par de párrafos contando qué es el producto, de dónde "
            "viene y por qué vale la pena. Este es el texto que más ayuda a vender "
            "y el que Google lee para posicionarte.\n\n"
            "Escribe como le hablarías a alguien en el mostrador: qué lo hace "
            "distinto, cómo se usa, con qué combina."
        ),
        "ficha": {
            "Contenido neto": "500 g",
            "Presentación": "Frasco de vidrio con tapa de seguridad",
            "Ingredientes": "100 % miel de abeja",
            "Conservación": "En lugar fresco y seco, lejos de la luz directa",
        },
        "origen": {
            "Región": "REEMPLAZAR con la región real",
            "Zona": "REEMPLAZAR con el valle o distrito",
            "Productor": "REEMPLAZAR o quitar esta fila",
        },
        "envio": {
            "Disponibilidad": "En stock",
            "Entrega en Lima": "24 a 48 horas",
            "Provincias": "3 a 5 días hábiles",
        },
    },

    {
        "id": 2, "slug": "quinua-organica-1kg", "mundo": "kay", "region": "sierra",
        "nombre": "Quinua orgánica 1 kg", "precio": 18.0,
        "icono": "grano", "foto": None, "etiqueta": "Orgánico",
        "desc": "Quinua real de Puno. Proteína completa, el grano de oro de los Andes.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 3, "slug": "maca-negra-polvo-250g", "mundo": "kay", "region": "sierra",
        "nombre": "Maca negra en polvo 250 g", "precio": 25.0,
        "icono": "raiz", "foto": None, "etiqueta": "Orgánico",
        "desc": "Maca de Junín, energía de altura. Superalimento tradicional.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 4, "slug": "aceite-sacha-inchi-250ml", "mundo": "kay", "region": "selva",
        "nombre": "Aceite de sacha inchi 250 ml", "precio": 45.0,
        "icono": "botella", "foto": None, "etiqueta": "Orgánico",
        "desc": "Omega 3 vegetal de la Amazonía peruana, prensado en frío.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 5, "slug": "cafe-tostado-altura-500g", "mundo": "kay", "region": "selva",
        "nombre": "Café tostado de altura 500 g", "precio": 32.0,
        "icono": "taza", "foto": None, "etiqueta": "Orgánico",
        "desc": "Café arábica de sombra, tueste medio, notas florales.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 6, "slug": "chia-organica-500g", "mundo": "kay", "region": "costa",
        "nombre": "Chía orgánica 500 g", "precio": 15.0,
        "icono": "grano", "foto": None, "etiqueta": "Orgánico",
        "desc": "Semillas de alto contenido en fibra para el día a día.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },

    # =====================================================================
    # HANAN PACHA — Importados
    # =====================================================================

    # ---- Catálogo real de bazar importado (APU Market) ----
    {
        "id": 25,
        "slug": "bufanda-tipo-cashmere",
        "mundo": "hanan",
        "region": None,
        "nombre": "Bufanda tipo cashmere",
        "precio": 18.0,
        "icono": "polo",
        "foto": "bufanda-cashmere-roja.webp",
        "etiqueta": "Importado",
        "desc": "Bufanda tipo cashmere con flecos, tejido suave para climas fríos. Varios colores.",
        "descripcion_larga": "",
        "ficha": {
            "Colores": "Rojo, rosado, gris y verde (Confirmar disponibilidad)",
            "Tejido": "Tipo cashmere, con flecos",
        },
        "origen": {"Importado por": "APU 3D Soluciones Integrales S.A.C."},
        "envio": {"Disponibilidad": "En stock", "Entrega en Lima": "24 a 48 horas", "Provincias": "3 a 5 días hábiles"},
    },
    {
        "id": 27, "slug": "gorro-lana-orejitas-animalito", "mundo": "hanan", "region": None,
        "nombre": "Gorro de lana orejitas (diseño animalito)", "precio": 10.0,
        "icono": "gorra", "foto": "gorro-lana-orejitas-animalito.webp", "etiqueta": "Importado",
        "desc": "Gorro tejido con orejeras, pompones y aplique de carita de animalito.",
        "descripcion_larga": "",
        "ficha": {"Color": "Mostaza"}, "origen": {}, "envio": {},
    },
    {
        "id": 28, "slug": "gorro-lana-pompon-oso", "mundo": "hanan", "region": None,
        "nombre": "Gorro de lana con pompón (diseño oso)", "precio": 10.0,
        "icono": "gorra", "foto": "gorro-lana-pompon-oso.webp", "etiqueta": "Importado",
        "desc": "Gorro tejido gris con diseño bordado de osito y pompón de peluche, franja azul.",
        "descripcion_larga": "",
        "ficha": {"Color": "Gris"}, "origen": {}, "envio": {},
    },
    {
        "id": 29, "slug": "estuche-organizador-viaje-rosa", "mundo": "hanan", "region": None,
        "nombre": "Estuche organizador de viaje rosa", "precio": 5.0,
        "icono": "funda", "foto": "estuche-organizador-viaje-rosa.webp", "etiqueta": "Importado",
        "desc": "Estuche compacto con cierre metálico, ideal para joyas o accesorios de viaje.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 30, "slug": "estuche-organizador-viaje-turquesa", "mundo": "hanan", "region": None,
        "nombre": "Estuche organizador de viaje turquesa", "precio": 5.0,
        "icono": "funda", "foto": "estuche-organizador-viaje-turquesa.webp", "etiqueta": "Importado",
        "desc": "Estuche compacto con doble cierre, color turquesa, para joyas o accesorios.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 31, "slug": "organizador-colgante-hello-animals", "mundo": "hanan", "region": None,
        "nombre": "Organizador colgante Hello Animals", "precio": 8.0,
        "icono": "funda", "foto": "organizador-colgante-hello-animals.webp", "etiqueta": "Importado",
        "desc": "Organizador de tela colgante con 3 bolsillos, diseño zorrito \"Hello Animals\".",
        "descripcion_larga": "",
        "ficha": {"Color": "Terracota"}, "origen": {}, "envio": {},
    },
    {
        "id": 32, "slug": "colitas-cabello-caja-flor", "mundo": "hanan", "region": None,
        "nombre": "Set de colitas para cabello (caja flor)", "precio": 4.0,
        "icono": "adorno", "foto": "colitas-cabello-caja-flor.webp", "etiqueta": "Importado",
        "desc": "Set surtido de colitas de cabello en estuche plástico en forma de flor, colores variados.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 33, "slug": "colitas-cabello-fashion", "mundo": "hanan", "region": None,
        "nombre": "Set de colitas para cabello Fashion", "precio": 3.0,
        "icono": "adorno", "foto": "colitas-cabello-fashion.webp", "etiqueta": "Importado",
        "desc": "Set de colitas de cabello acolchadas en empaque \"Fashion\", colores variados.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 34, "slug": "diadema-peluche-flor", "mundo": "hanan", "region": None,
        "nombre": "Diadema de peluche con flor", "precio": 8.0,
        "icono": "adorno", "foto": "diadema-peluche-flor.webp", "etiqueta": "Importado",
        "desc": "Diadema de peluche acolchada con aplique de flor.",
        "descripcion_larga": "",
        "ficha": {"Color": "Rosado"}, "origen": {}, "envio": {},
    },
    {
        "id": 35, "slug": "diadema-peluche-conejito", "mundo": "hanan", "region": None,
        "nombre": "Diadema de peluche conejito", "precio": 8.0,
        "icono": "adorno", "foto": "diadema-peluche-conejito.webp", "etiqueta": "Importado",
        "desc": "Diadema de peluche suave con aplique de conejito.",
        "descripcion_larga": "",
        "ficha": {"Color": "Lila"}, "origen": {}, "envio": {},
    },
    {
        "id": 36, "slug": "diadema-orejas-conejo", "mundo": "hanan", "region": None,
        "nombre": "Diadema de orejas de peluche", "precio": 8.0,
        "icono": "adorno", "foto": "diadema-orejas-conejo.webp", "etiqueta": "Importado",
        "desc": "Diadema de peluche con orejas largas tipo conejito, disponible en crema y rosado.",
        "descripcion_larga": "",
        "ficha": {"Color": "Crema / Rosado"}, "origen": {}, "envio": {},
    },
    {
        "id": 37, "slug": "encendedor-usb-recargable", "mundo": "hanan", "region": None,
        "nombre": "Encendedor USB recargable", "precio": 8.0,
        "icono": "regalo", "foto": "encendedor-usb-recargable.webp", "etiqueta": "Importado",
        "desc": "Encendedor de arco eléctrico recargable por USB, sin gas, ideal para cocina o parrilla.",
        "descripcion_larga": "",
        "ficha": {"Color": "Azul"}, "origen": {}, "envio": {},
    },
    {
        "id": 38, "slug": "cable-carga-magnetico-uslion", "mundo": "hanan", "region": None,
        "nombre": "Cable de carga magnético USLION", "precio": 15.0,
        "icono": "regalo", "foto": "cable-carga-magnetico-uslion.webp", "etiqueta": "Importado",
        "desc": "Cable de carga con conector magnético, marca USLION, disponible en varios colores (rojo, azul, verde, morado, negro, plateado).",
        "descripcion_larga": "",
        "ficha": {"Color": "Surtido"}, "origen": {}, "envio": {},
    },
    {
        "id": 39, "slug": "set-papeleria-mariposas", "mundo": "hanan", "region": None,
        "nombre": "Set de papelería mariposas", "precio": 3.0,
        "icono": "cuadro", "foto": "set-papeleria-mariposas.webp", "etiqueta": "Importado",
        "desc": "Set de papelería con block de notas, regla y stickers. También disponible en diseño panda.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },

    # =====================================================================
    # UKHU PACHA — Personalizados
    # =====================================================================

    # ---- EJEMPLO COMPLETO para un personalizado ----
    {
        "id": 13,
        "slug": "llavero-3d-personalizado",
        "mundo": "ukhu",
        "region": None,
        "nombre": "Llavero 3D personalizado",
        "precio": 20.0,
        "icono": "llavero",
        "foto": None,
        "etiqueta": "Personalizado",
        "desc": "Tu nombre, logo o figura impresos en PLA biodegradable.",
        "descripcion_larga": (
            "REEMPLAZAR. En personalizados lo decisivo es explicar CÓMO se pide: "
            "qué necesitas que te manden, en qué formato, cuánto demora y qué pasa "
            "si el cliente quiere cambios. Mientras más claro esté acá, menos "
            "preguntas repetidas te llegan por WhatsApp."
        ),
        "ficha": {
            "Material": "PLA biodegradable",
            "Medidas": "REEMPLAZAR",
            "Colores disponibles": "REEMPLAZAR",
            "Pedido mínimo": "1 unidad",
        },
        "origen": {
            "Producción": "Taller propio, Lima",
            "Técnica": "Impresión 3D por deposición fundida",
        },
        "envio": {
            "Disponibilidad": "Bajo pedido",
            "Tiempo de producción": "REEMPLAZAR: 2 a 3 días hábiles",
            "Qué necesitamos de ti": "El texto o el archivo del logo en PNG o SVG",
            "Entrega en Lima": "24 a 48 horas después de producido",
        },
    },

    {
        "id": 14, "slug": "taza-sublimada-con-foto", "mundo": "ukhu", "region": None,
        "nombre": "Taza sublimada con tu foto", "precio": 35.0,
        "icono": "taza", "foto": None, "etiqueta": "Personalizado",
        "desc": "Cerámica de alta calidad con impresión permanente a color.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 15, "slug": "polo-estampado-a-medida", "mundo": "ukhu", "region": None,
        "nombre": "Polo estampado a medida", "precio": 60.0,
        "icono": "polo", "foto": None, "etiqueta": "Personalizado",
        "desc": "Algodón peruano con tu diseño. Desde una unidad.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 16, "slug": "cuadro-topografico-relieve", "mundo": "ukhu", "region": None,
        "nombre": "Cuadro topográfico en relieve", "precio": 120.0,
        "icono": "cuadro", "foto": None, "etiqueta": "Personalizado",
        "desc": "El mapa en relieve del lugar que elijas, impreso en 3D.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 17, "slug": "funda-celular-personalizada", "mundo": "ukhu", "region": None,
        "nombre": "Funda de celular personalizada", "precio": 40.0,
        "icono": "funda", "foto": None, "etiqueta": "Personalizado",
        "desc": "Tu diseño sobre funda rígida. Compatible con la mayoría de modelos.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 18, "slug": "gorra-bordada-con-nombre", "mundo": "ukhu", "region": None,
        "nombre": "Gorra bordada con nombre", "precio": 55.0,
        "icono": "gorra", "foto": None, "etiqueta": "Personalizado",
        "desc": "Bordado profesional en hilo de color a elección.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },

    # =====================================================================
    # KUSI NAVIDAD 2026
    # La campaña atraviesa los tres mundos: cada producto declara de cuál viene.
    # =====================================================================

    {
        "id": 19, "slug": "canasta-kay-organica", "mundo": "kay", "region": None,
        "campana": True,
        "nombre": "Canasta Kay — orgánica", "precio": 150.0,
        "icono": "canasta", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Miel, café, quinua y chocolate de productores peruanos.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 20, "slug": "canasta-hanan-importada", "mundo": "hanan", "region": None,
        "campana": True,
        "nombre": "Canasta Hanan — selección importada", "precio": 350.0,
        "icono": "regalo", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Selección de productos importados en presentación de regalo.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 21, "slug": "adorno-navideno-personalizado", "mundo": "ukhu", "region": None,
        "campana": True,
        "nombre": "Adorno navideño personalizado", "precio": 80.0,
        "icono": "adorno", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Grabado con el nombre de cada persona de la familia.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 22, "slug": "retablo-ayacuchano-nacimiento", "mundo": "ukhu", "region": "sierra",
        "campana": True,
        "nombre": "Retablo ayacuchano — nacimiento andino", "precio": 180.0,
        "icono": "retablo", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Pieza hecha a mano por artesanos de Ayacucho. Edición limitada.",
        # Este es el producto más diferenciado del catálogo navideño.
        # Cuando lo cargues de verdad, nombra al artesano o taller: es su
        # trabajo y decirlo es parte de comprar bien.
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 23, "slug": "paneton-artesanal-masa-madre", "mundo": "kay", "region": "sierra",
        "campana": True,
        "nombre": "Panetón artesanal de masa madre", "precio": 85.0,
        "icono": "paneton", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Masa madre y frutos secos andinos. Horneado por encargo.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 24, "slug": "canasta-kimsa-tres-mundos", "mundo": "ukhu", "region": None,
        "campana": True,
        "nombre": "Canasta Kimsa — los tres mundos", "precio": 260.0,
        "icono": "kimsa", "foto": None, "etiqueta": "Kusi Navidad",
        "desc": "Una pieza de cada mundo: orgánico, importado y personalizado.",
        # Producto estrella de la campaña: es la prueba viva del concepto.
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
]


# ---------------------------------------------------------------------------
# Valores por defecto: evita que falte una clave y se caiga la página.
# No hace falta tocar esto.
# ---------------------------------------------------------------------------

_DEFECTOS = {
    "region": None, "foto": None, "campana": False,
    "descripcion_larga": "", "ficha": {}, "origen": {}, "envio": {},
}

for _p in PRODUCTOS:
    for _clave, _valor in _DEFECTOS.items():
        _p.setdefault(_clave, _valor)
