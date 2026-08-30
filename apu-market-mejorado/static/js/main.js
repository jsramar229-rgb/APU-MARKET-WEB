/* ==========================================================================
   APU MARKET — main.js
   Carrito en memoria + localStorage, navegación por tap, pedido por WhatsApp.
   ========================================================================== */

(function () {
  'use strict';

  var CLAVE = 'apu_carrito_v1';

  /* --- Iconos de mundo para el carrito (indican de qué mundo viene cada ítem) --- */
  var ICONO_MUNDO = {
    kay:  '<path d="M3 21h18"/><path d="M12 21V9"/><path d="M12 12C9 12 6.5 10 6.5 6.5 10 6.5 12 9 12 12z"/><path d="M12 14c3 0 5.5-2 5.5-5.5C14 8.5 12 11 12 14z"/>',
    hanan:'<circle cx="12" cy="5.5" r="2.6"/><path d="M2 20h20"/><path d="M3 20l6-8 3.5 4.6L15.5 13l5.5 7"/>',
    ukhu: '<path d="M12 2v20"/><path d="M12 8c-3.5 0-6-1.6-6-4.5"/><path d="M12 8c3.5 0 6-1.6 6-4.5"/><path d="M12 15c-2.6 0-4.6 1.4-5.4 3.6"/><path d="M12 15c2.6 0 4.6 1.4 5.4 3.6"/>'
  };

  function svgMundo(mundo) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" ' +
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
           (ICONO_MUNDO[mundo] || ICONO_MUNDO.kay) + '</svg>';
  }

  /* ---------------------------------------------------------------- estado */

  var carrito = [];

  function cargar() {
    try {
      var raw = localStorage.getItem(CLAVE);
      carrito = raw ? JSON.parse(raw) : [];
      if (!Array.isArray(carrito)) carrito = [];
    } catch (e) { carrito = []; }
  }

  function guardar() {
    try { localStorage.setItem(CLAVE, JSON.stringify(carrito)); } catch (e) { /* modo privado */ }
  }

  function soles(n) { return 'S/ ' + n.toFixed(2); }

  function total() {
    return carrito.reduce(function (s, i) { return s + i.precio * i.cant; }, 0);
  }

  function unidades() {
    return carrito.reduce(function (s, i) { return s + i.cant; }, 0);
  }

  /* -------------------------------------------------------------- carrito */

  window.agregar = function (id, nombre, precio, mundo, foto) {
    var item = carrito.filter(function (i) { return i.id === id; })[0];
    if (item) {
      item.cant += 1;
      if (foto) item.foto = foto;
    }
    else { carrito.push({ id: id, nombre: nombre, precio: precio, mundo: mundo, foto: foto || '', cant: 1 }); }
    guardar();
    pintar();
    toast(nombre + ' agregado');
  };

  window.cambiarCantidad = function (id, delta) {
    var item = carrito.filter(function (i) { return i.id === id; })[0];
    if (!item) return;
    item.cant += delta;
    if (item.cant < 1) { return window.quitar(id); }
    guardar();
    pintar();
  };

  window.quitar = function (id) {
    carrito = carrito.filter(function (i) { return i.id !== id; });
    guardar();
    pintar();
  };

  function pintar() {
    var badge = document.getElementById('badge');
    var cuerpo = document.getElementById('carritoCuerpo');
    var pie = document.getElementById('carritoPie');
    if (badge) badge.textContent = unidades();
    if (!cuerpo) return;

    if (!carrito.length) {
      cuerpo.innerHTML =
        '<div class="carrito-vacio">' + svgMundo('kay') +
        '<p>Tu carrito está vacío</p>' +
        '<p style="font-size:.85rem;margin-top:6px">Explora los tres mundos y encuentra algo especial.</p></div>';
      if (pie) pie.hidden = true;
      return;
    }

    cuerpo.innerHTML = carrito.map(function (i) {
      return '' +
        '<div class="carrito-item">' +
          '<div class="carrito-item-visual ' + i.mundo + '">' +
            (i.foto ? '<img src="/static/img/productos/' + escapar(i.foto) + '" alt="" loading="lazy">' : svgMundo(i.mundo)) +
          '</div>' +
          '<div class="carrito-item-info">' +
            '<p class="carrito-item-nombre">' + escapar(i.nombre) + '</p>' +
            '<p class="carrito-item-precio">' + soles(i.precio) + ' c/u</p>' +
            '<div class="cantidad">' +
              '<button type="button" class="js-menos" data-id="' + i.id + '" aria-label="Quitar una unidad">−</button>' +
              '<span>' + i.cant + '</span>' +
              '<button type="button" class="js-mas" data-id="' + i.id + '" aria-label="Agregar una unidad">+</button>' +
            '</div>' +
            '<button type="button" class="carrito-quitar js-quitar" data-id="' + i.id + '">Eliminar</button>' +
          '</div>' +
          '<div style="font-weight:600;font-size:.9rem;white-space:nowrap">' + soles(i.precio * i.cant) + '</div>' +
        '</div>';
    }).join('');

    var t = document.getElementById('carritoTotal');
    if (t) t.textContent = soles(total());
    if (pie) pie.hidden = false;
  }

  function escapar(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* ------------------------------------------------------------- drawer */

  window.abrirCarrito = function () {
    document.getElementById('carrito').classList.add('abierto');
    document.getElementById('carritoFondo').classList.add('abierto');
    document.body.style.overflow = 'hidden';
  };

  window.cerrarCarrito = function () {
    document.getElementById('carrito').classList.remove('abierto');
    document.getElementById('carritoFondo').classList.remove('abierto');
    document.body.style.overflow = '';
  };

  /* ------------------------------------------------------------ whatsapp */

  window.pedirPorWhatsApp = function () {
    if (!carrito.length) { toast('Tu carrito está vacío'); return; }

    var lineas = carrito.map(function (i) {
      return '• ' + i.nombre + ' × ' + i.cant + ' — ' + soles(i.precio * i.cant);
    }).join('\n');

    var selector = document.getElementById('metodoPago');
    var metodo = selector && selector.value ? selector.value : 'Aún por coordinar';
    var texto =
      '¡Hola APU Market! Quiero hacer este pedido:\n\n' + lineas +
      '\n\n*Total: ' + soles(total()) + '*\n' +
      '*Método de pago preferido:* ' + metodo + '\n\n' +
      '¿Cómo coordinamos el pago y el envío?';

    window.open('https://wa.me/' + window.APU.whatsapp + '?text=' + encodeURIComponent(texto), '_blank');
  };

  /* --------------------------------------------------------------- toast */

  var tToast;
  function toast(msg) {
    var el = document.getElementById('toast');
    var txt = document.getElementById('toastMsg');
    if (!el || !txt) return;
    txt.textContent = msg;
    el.classList.add('visible');
    clearTimeout(tToast);
    tToast = setTimeout(function () { el.classList.remove('visible'); }, 2600);
  }

  /* ---------------------------------------------------------- navegación */

  function initNav() {
    var btn = document.getElementById('btnMundos');
    var menu = document.getElementById('menuMundos');
    var toggle = document.getElementById('menuToggle');
    var nav = document.getElementById('nav');

    /* Desplegable por TAP, no por hover: la mayoría del tráfico es móvil
       y en móvil el hover simplemente no existe. */
    if (btn && menu) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var abierto = menu.classList.toggle('abierto');
        btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      });
      document.addEventListener('click', function (e) {
        if (!menu.contains(e.target) && e.target !== btn) {
          menu.classList.remove('abierto');
          btn.setAttribute('aria-expanded', 'false');
        }
      });
    }

    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var abierto = nav.classList.toggle('abierto');
        toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
        document.body.style.overflow = abierto ? 'hidden' : '';
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      if (menu) { menu.classList.remove('abierto'); }
      if (btn) { btn.setAttribute('aria-expanded', 'false'); }
      if (nav) { nav.classList.remove('abierto'); }
      if (toggle) { toggle.setAttribute('aria-expanded', 'false'); }
      window.cerrarCarrito();
    });
  }

  /* ------------------------------------------------- delegación de eventos */

  function initAcciones() {
    document.addEventListener('click', function (e) {
      if (!e.target.closest) return;

      var add = e.target.closest('.js-agregar');
      if (add) {
        window.agregar(
          parseInt(add.dataset.id, 10),
          add.dataset.nombre,
          parseFloat(add.dataset.precio),
          add.dataset.mundo,
          add.dataset.foto
        );
        return;
      }
      var mas = e.target.closest('.js-mas');
      if (mas) { window.cambiarCantidad(parseInt(mas.dataset.id, 10), 1); return; }

      var menos = e.target.closest('.js-menos');
      if (menos) { window.cambiarCantidad(parseInt(menos.dataset.id, 10), -1); return; }

      var quita = e.target.closest('.js-quitar');
      if (quita) { window.quitar(parseInt(quita.dataset.id, 10)); }
    });
  }

  /* ----------------------------------------------------------------- init */

  document.addEventListener('DOMContentLoaded', function () {
    cargar();
    pintar();
    initNav();
    initAcciones();
  });

})();
