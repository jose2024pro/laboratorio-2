// script.js

            
            function mostrarImagen(event) {
                const imagen = document.getElementById('ver-imagen'); 
                imagen.src = URL.createObjectURL(event.target.files[0]); 
                imagen.style.display = 'block'; 
            }
            
          
            document.getElementById('registroForm').addEventListener('submit', function(event) {
                
                const nombre = document.querySelector('input[name="nombre"]').value;
                const email = document.querySelector('input[name="email"]').value;
                const password = document.querySelector('input[name="password"]').value;
                
                function validarNombre(n){
                    
                    const contieneNumero = /\d/.test(n); 
                    return contieneNumero;  
                }
                
                if (nombre === '' || email === '' || password === '') {
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
           