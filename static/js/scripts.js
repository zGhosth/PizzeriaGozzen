const carrito = {};

function agregarCarrito(nombre, precio) {
    if (carrito[pizza]) {
        carrito[pizza].cantidad++;
    } else {
        carrito[pizza] = { cantidad: 1, precio: precio };
    }

    mostrarCarrito();
}



function mostrarCarrito() {
    const listaCarrito = document.getElementById('lista-carrito');
    const totalCarrito = document.getElementById('total-carrito');
    listaCarrito.innerHTML = '';
    let total = 0;

    Object.keys(carrito).forEach(pizza => {
        const item = carrito[pizza];
        const subtotal = item.precio * item.cantidad;
        total += subtotal;

        const div = document.createElement('div');
        div.className = 'list-group-item d-flex justify-content-between align-items-center';

        div.innerHTML = `
            <span>${pizza} (x${item.cantidad})</span>
            <span>$${subtotal}</span>
        `;

        listaCarrito.appendChild(div);
    });

    // Mostrar el total solo si el elemento existe
    if (totalCarrito) {
        totalCarrito.textContent = `Total: $${total}`;
    } else {
        console.error("No se encontró el elemento #total-carrito");
    }

    
}
