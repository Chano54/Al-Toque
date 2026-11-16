# Al Toque (nombre temporal)

Pide tu trago en la discoteca desde el celular, sin hacer cola. El cliente escanea un QR, pide y paga; la barra recibe el pedido; cuando está listo, el celular del cliente vibra y le muestra un QR que el bartender escanea para entregar.

**Demo en vivo:** https://chano54.github.io/Al-Toque/

## Qué tiene la demo
- **Cliente:** carta, tiempo de espera según qué tan llena está la barra, pago simulado con Yape (número + código de aprobación) o tarjeta (se puede guardar), y aviso con QR cuando el pedido está listo.
- **Cobro:** Yape se cobra al pedir. Con tarjeta el monto solo se separa y se cobra cuando la barra escanea el QR al entregar (si no se recoge en 30 min, se cobra igual). Se puede cancelar solo antes de que la barra empiece a preparar; si cancela o la barra no puede hacerlo, se devuelve o libera todo. Servicio Al Toque: S/1 por trago, lo paga el cliente.
- **Barra:** medidor de saturación con pausa, pedidos nuevos / en preparación / para recoger, y escáner de QR con la cámara (un QR usado se rechaza; si no lee, se escribe el código de 3 letras).
- **Dueño:** ventas, lo más pedido, espera promedio, capacidad de la barra y edición de carta y precios.

Por ahora los datos viven en el navegador (sirve para mostrar la demo en un equipo). Falta un servidor para conectar varios celulares y el pago real.

## Cómo se arma
El código está en `src/`. `python3 src/build.py` genera el `index.html` de la raíz (un solo archivo, con las librerías incluidas).

Librerías: [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) (MIT) y [jsQR](https://github.com/cozmo/jsQR) (Apache-2.0).
