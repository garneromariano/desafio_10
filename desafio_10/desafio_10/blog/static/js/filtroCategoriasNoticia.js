document.addEventListener("DOMContentLoaded", function() {
    // Capturar el evento de cambio en el combobox
    document.getElementById("select-categoria").addEventListener("change", function() {
        // Obtener el valor seleccionado
        var categoriaSeleccionada = this.value;
        if (categoriaSeleccionada === "") {
            // Si la opción seleccionada es "Todas", redireccionar a la misma página sin el parámetro "categoria"
            window.location.href = "{% url 'noticias:listar_noticias' %}";
        } else {
            // Redireccionar a la URL con el parámetro de categoría seleccionada
            var baseURL = window.location.protocol + "//" + window.location.host;
            var urlCompleto = baseURL + "/noticias/listar/?categoria=" + categoriaSeleccionada;
           
            window.location.href = urlCompleto;
            //window.location.href = "{% url 'noticias:listar_noticias' %}?categoria=" + categoriaSeleccionada;
        }
    });
});