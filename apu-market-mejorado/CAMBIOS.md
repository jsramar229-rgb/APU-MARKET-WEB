# APU Market — mejoras incorporadas

Se conservaron Flask, Jinja, el catálogo separado y el flujo existente por WhatsApp. La versión mejorada incorpora fotografías referenciales cuadradas, miniaturas en el carrito, fichas ampliadas para productos representativos y una presentación más clara del pago y el envío.

## Cambios principales

La portada ahora comunica tres alternativas de pago: Yape o Plin, transferencia bancaria y contra entrega. En cada ficha de producto aparece el bloque **Compra acompañada**, que explica que la disponibilidad, el envío y los datos de pago se confirman por WhatsApp antes del cobro.

El carrito ahora permite elegir un método de pago preferido. Esa selección se incluye automáticamente en el mensaje de WhatsApp junto con los productos, cantidades y total. También conserva la fotografía del producto como miniatura cuando está disponible.

Se completaron fichas editoriales de miel, café, audífonos, llavero 3D, retablo ayacuchano y canasta Kimsa. La información que aún requiere validación se marca como “Confirmar” para evitar publicar datos comerciales no verificados.

## Antes de publicar

Reemplaza el número de WhatsApp, correo, RUC y datos de empresa en `app.py`. Cambia las opciones y descripciones de `PAGOS` en el mismo archivo según los métodos realmente disponibles. Revisa precios, stock, garantías, tiempos y procedencias en `catalogo.py`.

Las seis imágenes incorporadas son **referenciales** para probar la interfaz. Deben reemplazarse por fotografías propias de APU Market o por recursos cuya licencia comercial haya sido confirmada. La lista de fuentes y las recomendaciones de formato están en `static/img/productos/LEEME.txt`.

## Ejecución local

```bash
pip install -r requirements.txt
python app.py
```

Luego abre `http://127.0.0.1:5000`. Para una prueba real de pedidos, cambia primero el WhatsApp de marcador en `app.py`.
