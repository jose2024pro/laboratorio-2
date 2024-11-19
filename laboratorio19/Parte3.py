#Parte3 - diccionario
calificaciones = {"Juan": "5.0", "Andres": "4.1", "Ana": "3.0"}
nombre_max = max(calificaciones, key=calificaciones.get) 
print(f' El estudiante con la mayor nota es {nombre_max} y su calificacion es de {calificaciones[nombre_max]}.')