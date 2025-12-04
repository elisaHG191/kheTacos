// main.js

function nuevaOrden() {
    // Aquí podrías redirigir a un formulario de Django
    // window.location.href = "/ordenes/nueva/";
    
    alert("Redirigiendo al formulario para crear una nueva orden...");
    console.log("Click en Nueva Orden detectado");
}

// Opcional: Animación simple para los números al cargar
document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.number');
    
    counters.forEach(counter => {
        const target = +counter.innerText; // Obtener el número final
        if(target > 0) {
            let count = 0;
            const increment = target / 20; // velocidad
            
            const updateCount = () => {
                count += increment;
                if(count < target) {
                    counter.innerText = Math.ceil(count);
                    setTimeout(updateCount, 40);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        }
    });
});