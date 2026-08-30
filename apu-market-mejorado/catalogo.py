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
        "foto": "miel-de-abeja-andina.jpg",        # foto referencial; reemplazar por foto propia
        "etiqueta": "Orgánico",
        "desc": "Miel pura de valles andinos, cosechada artesanalmente y sin aditivos.",
        "descripcion_larga": (
            "Miel de textura suave y sabor naturalmente dulce para acompañar desayunos, "
            "infusiones y preparaciones caseras. La fotografía es referencial hasta contar "
            "con la imagen del frasco y la etiqueta de la presentación disponible.\n\n"
            "Antes de publicar, confirma con el productor la zona exacta de procedencia, "
            "el lote y la fecha de cosecha para comunicar la información con transparencia."
        ),
        "ficha": {
            "Contenido neto": "500 g",
            "Presentación": "Frasco de vidrio con tapa de seguridad",
            "Ingredientes": "100 % miel de abeja",
            "Conservación": "En lugar fresco y seco, lejos de la luz directa",
        },
        "origen": {
            "Región": "Sierra del Perú",
            "Zona": "Confirmar valle o distrito de procedencia",
            "Productor": "Confirmar nombre del productor o cooperativa",
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
        "icono": "taza", "foto": "cafe-tostado-altura.jpg", "etiqueta": "Orgánico",
        "desc": "Café arábica de sombra, tueste medio, notas florales.",
        "descripcion_larga": (
            "Un café de perfil aromático y tueste medio para disfrutar en casa, en prensa, "
            "cafetera o método filtrado. La imagen es referencial hasta contar con la foto "
            "del empaque real.\n\n"
            "Confirma la fecha de tostado, la presentación disponible y la procedencia exacta "
            "con APU Market antes de realizar el pago."
        ),
        "ficha": {
            "Contenido neto": "500 g",
            "Tipo": "Café arábica de sombra",
            "Tueste": "Medio",
            "Preparación": "Filtrado, prensa francesa o cafetera",
        },
        "origen": {"Región declarada": "Selva del Perú", "Procedencia exacta": "Confirmar antes de publicar"},
        "envio": {"Disponibilidad": "Confirmar stock", "Entrega en Lima": "24 a 48 horas", "Provincias": "3 a 5 días hábiles"},
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

    # ---- EJEMPLO COMPLETO para un importado ----
    {
        "id": 7,
        "slug": "audifonos-cancelacion-ruido",
        "mundo": "hanan",
        "region": None,
        "nombre": "Audífonos con cancelación de ruido",
        "precio": 320.0,
        "icono": "audifonos",
        "foto": "audifonos-cancelacion-ruido.jpg",
        "etiqueta": "Importado",
        "desc": "Cancelación activa, batería de larga duración y estuche de carga.",
        "descripcion_larga": (
            "Audífonos inalámbricos pensados para concentrarte, viajar o escuchar música "
            "con mayor comodidad. La fotografía es referencial hasta contar con la imagen "
            "del modelo exacto que se encuentre disponible.\n\n"
            "Antes de pagar, confirma el modelo, el color, la fecha de entrega y el plazo "
            "de garantía aplicable a tu compra."
        ),
        "ficha": {
            "Marca y modelo": "Confirmar modelo disponible",
            "Conectividad": "Bluetooth 5.3",
            "Autonomía": "Hasta 30 horas con estuche (confirmar modelo)",
            "Incluye": "Estuche de carga, cable USB-C, almohadillas de repuesto",
            "Garantía": "Confirmar plazo y condiciones antes de publicar",
        },
        "origen": {
            "Procedencia": "Confirmar país de importación",
            "Importado por": "APU 3D Soluciones Integrales S.A.C.",
        },
        "envio": {
            "Disponibilidad": "Confirmar stock o pedido especial",
            "Entrega en Lima": "24 a 48 horas",
            "Provincias": "3 a 5 días hábiles",
        },
    },

    {
        "id": 8, "slug": "reloj-inteligente-deportivo", "mundo": "hanan", "region": None,
        "nombre": "Reloj inteligente deportivo", "precio": 280.0,
        "icono": "reloj", "foto": None, "etiqueta": "Importado",
        "desc": "Monitor de actividad y sueño, GPS integrado, resistente al agua.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 9, "slug": "proyector-portatil-full-hd", "mundo": "hanan", "region": None,
        "nombre": "Proyector portátil full HD", "precio": 420.0,
        "icono": "proyector", "foto": None, "etiqueta": "Importado",
        "desc": "Cine en casa. Se conecta al celular por cable o de forma inalámbrica.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 10, "slug": "camara-accion-4k", "mundo": "hanan", "region": None,
        "nombre": "Cámara de acción 4K", "precio": 380.0,
        "icono": "camara", "foto": None, "etiqueta": "Importado",
        "desc": "Estabilización electrónica y carcasa sumergible para exteriores.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 11, "slug": "tableta-grafica-con-lapiz", "mundo": "hanan", "region": None,
        "nombre": "Tableta gráfica con lápiz", "precio": 260.0,
        "icono": "tableta", "foto": None, "etiqueta": "Importado",
        "desc": "Superficie sensible a la presión para dibujo y diseño digital.",
        "descripcion_larga": "",
        "ficha": {}, "origen": {}, "envio": {},
    },
    {
        "id": 12, "slug": "parlante-inalambrico-resistente-agua", "mundo": "hanan", "region": None,
        "nombre": "Parlante inalámbrico resistente al agua", "precio": 190.0,
        "icono": "parlante", "foto": None, "etiqueta": "Importado",
        "desc": "Sonido envolvente, doce horas de autonomía, uso en exteriores.",
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
        "foto": "llavero-3d-personalizado.jpg",
        "etiqueta": "Personalizado",
        "desc": "Tu nombre, logo o figura impresos en PLA biodegradable.",
        "descripcion_larga": (
            "Convierte tu nombre, logo o figura en un pequeño objeto hecho a tu medida. "
            "Envíanos la idea, el texto o el archivo de referencia y te confirmaremos la "
            "viabilidad, los colores y el acabado antes de producirlo.\n\n"
            "Recibirás una confirmación del diseño, precio y plazo por WhatsApp. La imagen "
            "es referencial: el resultado final depende del archivo y las medidas acordadas."
        ),
        "ficha": {
            "Material": "PLA biodegradable",
            "Medidas": "Confirmar según el diseño",
            "Colores disponibles": "Consultar colores disponibles",
            "Pedido mínimo": "1 unidad",
        },
        "origen": {
            "Producción": "Taller propio, Lima",
            "Técnica": "Impresión 3D por deposición fundida",
        },
        "envio": {
            "Disponibilidad": "Bajo pedido",
            "Tiempo de producción": "Confirmar: normalmente 2 a 3 días hábiles",
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
        "icono": "retablo", "foto": "retablo-ayacuchano-nacimiento.jpg", "etiqueta": "Kusi Navidad",
        "desc": "Pieza hecha a mano por artesanos de Ayacucho. Edición limitada.",
        # Este es el producto más diferenciado del catálogo navideño.
        # Cuando lo cargues de verdad, nombra al artesano o taller: es su
        # trabajo y decirlo es parte de comprar bien.
        "descripcion_larga": (
            "Una pieza decorativa para celebrar la Navidad desde una mirada andina. "
            "Cada retablo puede presentar variaciones propias del trabajo manual, por lo que "
            "la imagen debe considerarse referencial hasta contar con la pieza disponible."
        ),
        "ficha": {
            "Técnica": "Retablo artesanal",
            "Tema": "Nacimiento andino",
            "Edición": "Limitada",
            "Medidas": "Confirmar pieza disponible",
        },
        "origen": {"Región": "Ayacucho, Perú", "Artesano o taller": "Confirmar antes de publicar"},
        "envio": {"Disponibilidad": "Edición limitada — confirmar stock", "Entrega en Lima": "24 a 48 horas", "Provincias": "3 a 5 días hábiles"},
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
        "icono": "kimsa", "foto": "canasta-kimsa-tres-mundos.jpeg", "etiqueta": "Kusi Navidad",
        "desc": "Una pieza de cada mundo: orgánico, importado y personalizado.",
        # Producto estrella de la campaña: es la prueba viva del concepto.
        "descripcion_larga": (
            "Una selección de regalo que reúne la propuesta de APU Market en una sola caja: "
            "un detalle orgánico, uno importado y una pieza personalizada. El contenido final "
            "se confirma contigo por WhatsApp según disponibilidad y presupuesto."
        ),
        "ficha": {
            "Contenido": "Una selección de los tres mundos",
            "Presentación": "Canasta o empaque de regalo",
            "Personalización": "Consultar opciones disponibles",
        },
        "origen": {"Selección": "Productos peruanos e importados según disponibilidad"},
        "envio": {"Disponibilidad": "Preventa — confirmar fecha de entrega", "Entrega en Lima": "Coordinar por WhatsApp", "Provincias": "Consultar cobertura"},
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
