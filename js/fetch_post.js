let submitButton = document.querySelector("#contactForm #Crear");

submitButton.addEventListener("click", ()=>{
    let data_post = {
        'nombre': document.querySelector("#contactForm #nombre").value,
        'email': document.querySelector("#contactForm #email").value,
        'telefono': document.querySelector("#contactForm #telefono").value,
        'asunto': document.querySelector("#contactForm #asunto").value,
        'mensaje': document.querySelector("#contactForm #mensaje").value
        
    }
    
    fetchData(
        "http://localhost:5000/api/client/create/",
        "POST",
        (data) => {
            document.querySelector("#contactForm").reset();
            window.location.replace("../pages/clientes.html");
        },
        data_post
    );
    
    }
);

