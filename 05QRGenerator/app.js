const contenedorQR = document.getElementById('qrContainer');
const formulario = document.getElementById('qrForm');

const QR = new QRCode(contenedorQR);

formulario.addEventListener('submit', (e) => {
	e.preventDefault();
	QR.makeCode(formulario.link.value);
});