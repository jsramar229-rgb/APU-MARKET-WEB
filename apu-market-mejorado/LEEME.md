# APU MARKET — versión unificada

Ensamble de las tres versiones generadas (Qwen, Kimi, Z.ai) sobre el sistema visual
Paracas–Chavín–Chachapoyas.

## Cómo correrlo

```powershell
cd D:\APU-MARKET-WEB\apu-market-unificado
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Luego abrir http://127.0.0.1:5000

**Flask cachea las plantillas al arrancar.** Después de editar un `.html` o un `.py` hay que
**reiniciar** el servidor (Ctrl+C y volver a `python app.py`), no basta con refrescar.

---

## Dónde va cada cosa

| Quiero cambiar… | Voy a… |
|---|---|
| Precios, nombres, descripciones, fotos | `catalogo.py` |
| WhatsApp, RUC, correo, horario | `app.py` → dict `EMPRESA` |
| Encender o apagar la campaña | `app.py` → `CAMPANA["activa"]` |
| Las fotos de producto | `static/img/productos/` |
| Colores, tipografía, espaciados | `static/css/style.css` |

**El catálogo está aparte a propósito.** Cambiar un precio no debería obligarte a abrir el
archivo de la aplicación. Se quedó en Python y no en JSON porque JSON no admite comentarios
—y vas a querer anotar "falta foto" o "confirmar precio"— y porque su sintaxis es más
estricta: prohíbe la coma final, que es justo el error que uno comete agregando productos.

---

## Agregar fotos de producto

1. Guarda la foto en `static/img/productos/`
2. En `catalogo.py`, cambia `"foto": None` por `"foto": "nombre-del-archivo.webp"`

Mientras el campo esté en `None` se muestra el icono de respaldo. **Nada se rompe si falta
una foto**, así que puedes ir cargándolas de a pocas. Las especificaciones completas están en
`static/img/productos/LEEME.txt`; en resumen: cuadradas de 1000×1000, menos de 150 KB, WebP,
y fotografiadas sobre fondo crema `#F4EFE4` para que la grilla se vea pareja.

## Agregar el detalle de un producto

Cada producto tiene cuatro bloques opcionales. Los que dejes vacíos simplemente no se dibujan:

- `descripcion_larga` — párrafos separados por una línea en blanco. Es lo que más vende y lo
  que Google lee.
- `ficha` — peso, presentación, ingredientes o materiales, garantía.
- `origen` — región, zona, productor o taller.
- `envio` — disponibilidad, tiempos, qué necesitas del cliente. Este también aparece resumido
  arriba, junto al precio.

`ficha`, `origen` y `envio` son diccionarios libres: la clave es la etiqueta visible y el
valor es el dato. Pon las filas que quieras.

> **Los textos de detalle vienen casi todos vacíos a propósito.** No inventé orígenes,
> productores ni composiciones: publicar datos inventados sobre el origen de un alimento es
> una afirmación falsa frente al consumidor y ante INDECOPI. Los productos con id 1, 7 y 13
> están marcados como EJEMPLO y muestran el formato.

---

## Subir a GitHub (hacerlo ANTES de cargar el catálogo)

Cargar 24 productos con fotos y textos es trabajo de varias horas. Hacerlo con el
repositorio ya creado significa que cada paso queda guardado y se puede deshacer.

```powershell
cd D:\APU-MARKET-WEB\apu-market-unificado
git init
git add .
git status          # <-- REVISAR: que NO aparezca venv/ en la lista
git commit -m "Version inicial de APU Market"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/apu-market.git
git push -u origin main
```

Crea el repositorio en GitHub como **privado**. El `.gitignore` ya está listo y excluye
`venv/`, `__pycache__/` y `.env` — por eso el `git status` antes del commit: si ahí aparece
`venv/`, algo salió mal y hay que corregirlo antes de subir, porque son miles de archivos.

De ahí en adelante, cada cambio son tres líneas:

```powershell
git add .
git commit -m "Agrego fotos de Kay Pacha"
git push
```

### Conectar con Render

En Render: **New → Web Service → conectar el repositorio**, y configurar:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

Cada `git push` vuelve a desplegar sola la web.

**Plan pago antes de octubre.** El gratuito duerme a los 15 minutos sin tráfico y tarda cerca
de un minuto en despertar: un cliente que entra de noche por un enlace de WhatsApp no espera
un minuto en blanco.

### Nunca subir secretos

Hoy no hay ninguno. Cuando conectes el Libro de Reclamaciones a un correo real, esa contraseña
va en las **variables de entorno de Render**, jamás en el código.

---

## Estructura

```
app.py                    configuración (EMPRESA, CAMPANA) y rutas
catalogo.py               EL CATÁLOGO — aquí editas productos
requirements.txt          Flask + gunicorn
.gitignore
templates/
  base.html               header, footer, carrito, toast
  _iconos.html            marca (cabeza clava) e iconografía
  _componentes.html       tarjeta de producto, grilla, tablas de datos
  index.html              portada
  mundo.html              plantilla única para los tres mundos
  producto.html           ficha de producto
  campana.html            Kusi Navidad
  campana_cerrada.html    fuera de temporada
  nosotros.html
  reclamaciones.html      Libro de Reclamaciones Virtual
  404.html
static/
  css/style.css
  js/main.js              carrito, navegación, pedido por WhatsApp
  img/productos/          fotos (ver LEEME.txt ahí dentro)
```

## Rutas

| Dirección | Qué es |
|---|---|
| `/` | Portada |
| `/kay-pacha` `/hanan-pacha` `/ukhu-pacha` | Los tres mundos |
| `/kay-pacha?region=sierra` | Filtro de origen (solo Kay Pacha) |
| `/producto/<slug>` | Ficha de producto |
| `/kusi-navidad` | Campaña (404 si está apagada) |
| `/nosotros` · `/libro-de-reclamaciones` | |

---

## PENDIENTES antes de publicar

1. **Datos reales** en `EMPRESA`: RUC, WhatsApp (hoy `51999999999`, marcador), correo.
2. **Catálogo real** con fotos propias y textos de detalle.
3. **Libro de Reclamaciones**: el formulario cumple los campos de INDECOPI pero hoy solo
   confirma en pantalla. Falta conectarlo a un correo — la constancia al consumidor es
   obligatoria.
4. **Textos legales**: términos, privacidad, envíos y devoluciones están enlazados pero vacíos.
5. **Comprobantes electrónicos**: resolver el flujo de emisión de boletas (SEE-SOL de SUNAT
   sirve para empezar) antes de la campaña.

## Accesibilidad

Los pares de color están verificados contra WCAG AA. El ocre `#B4831F` **no** pasa contraste
como texto sobre crema (2.95:1): existe solo para acentos, bordes y patrones. Para texto
dorado sobre fondo claro está `--oro-texto` (`#8A6314`). Sobre fondo oscuro, el botón oscuro
desaparece: ahí va `.btn-oro`.

## Dos errores ya corregidos — no reintroducirlos

1. **`tojson` dentro de un atributo HTML.** Rompe el atributo cuando el texto lleva comillas y
   deja el botón muerto. Los datos van en atributos `data-` con delegación de eventos.
2. **`flex-shrink: 0` en la marca del header.** Desbordaba el header en móvil y ponía el botón
   del carrito encima del de menú, bloqueándolo.
