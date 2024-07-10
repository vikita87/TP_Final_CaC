// Contenedor donde se muestran los clientes
let clientContainer = document.querySelector(".clientes-container");

// Template de clientes registrados
let allClientsTemplateReference = document.querySelector(".clientes-registrados");

let allClient = allClientsTemplateReference.cloneNode(true);

// Quito del documento los templates
allClientsTemplateReference.remove();

fetchData(
    "http://localhost:5000/api/clients/all",
    "GET",
    (data) => {
        console.log(data);

        let clientes = [];

        // Recorro la lista de clientes registrados
        for (const cliente of data) {
            //console.log(tarea);

            // Duplico la plantilla de clientes registrados
            let newClient = allClient.cloneNode(true);

            // Completo la lista de clientes registrados
            newClient.querySelector(".nombre").innerHTML = cliente.nombre;
            newClient.querySelector(".email").innerHTML = cliente.email;
            newClient.querySelector(".telefono").innerHTML = cliente.telefono;
            newClient.querySelector(".asunto").innerHTML = cliente.asunto;
            newClient.querySelector(".mensaje").innerHTML = cliente.mensaje;

            // Agrego la nueva tarea al listado de tareas para ver en el viewport
            clientes.push(newClient);
        }

        // Accion doble: 
        // ReplaceChildren borra todo el contenido interno y agrega lo que yo le diga
        clientContainer.replaceChildren(...clientes);
    }
    );