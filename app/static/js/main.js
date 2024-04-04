// ENVIA EL INPUT A FLASK. 
document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("console-form");
    var consoleContainer = document.querySelector(".contenido-game");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        var formData = new FormData(form);
        var texto = formData.get("texto");

        fetch("/", {
            method: "POST",
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                var messageElement = document.createElement("p");
                messageElement.textContent = texto;
                consoleContainer.appendChild(messageElement);
                // Limpia el campo de entrada
                form.reset();
            })
            .catch(error => console.error("Error:", error));
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("console-form");
    var consoleContainer = document.querySelector(".contenido-game");

    // Recuperar todos los datos guardados del localStorage
    var datosGuardados = JSON.parse(localStorage.getItem("datos")) || { textos: [], respuestas: [] };

    // Mostrar todos los textos y respuestas guardados en la consola
    for (var i = 0; i < datosGuardados.textos.length; i++) {
        var textoElement = document.createElement("p");
        textoElement.textContent = datosGuardados.textos[i];
        consoleContainer.appendChild(textoElement);

        var respuestaElement = document.createElement("p");
        respuestaElement.textContent = datosGuardados.respuestas[i];
        consoleContainer.appendChild(respuestaElement);
    }

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var formData = new FormData(form);
        var texto = formData.get("texto");

        fetch("/mensaje", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            var mensaje = data.mensaje;
            var messageElement = document.createElement("p");
            messageElement.textContent = mensaje;
            consoleContainer.appendChild(messageElement);

            // Agregar el nuevo texto y respuesta a los datos guardados
            datosGuardados.textos.push(texto);
            datosGuardados.respuestas.push(mensaje);

            // Guardar todos los datos en localStorage
            localStorage.setItem("datos", JSON.stringify(datosGuardados));

            // Limpia el campo de entrada
            form.reset();
        })
        .catch(error => console.error("Error:", error));
    });
});



