// script.js

function mostrarMensaje(){
    alert('Bienvenido a mi Hoja de Vida');
}
           
        
            document.getElementById('registroForm').addEventListener('submit', function(event) {
                
                const nombre = document.querySelector('input[name="nombre"]').value;
                const email = document.querySelector('input[name="email"]').value;
                
                
                function validarNombre(n){
                    
                    const contieneNumero = /\d/.test(n); 
                    return contieneNumero;  
                }
                
                if (nombre === '' || email === '') {
                    alert('Por favor completa todos los campos.'); 
                    event.preventDefault(); 
                } else{ 
                    if(validarNombre(nombre)){
                    alert('El nombre no debe contener numeros'); 
                    event.preventDefault(); 
                    console.log("el nombre tiene numeros debe salirse")
                    }else{
                    alert('Registro exitoso'); 
                    }
                }
            });
           