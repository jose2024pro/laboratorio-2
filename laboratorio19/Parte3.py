#Parte3 - diccionario
calificaciones = {"Juan": 5.0, "Andres": 4.1, "Ana": 3.0}
estudiant=""
nota_mayor=1
print("Lista de los estudiantes")
for estudiante, cal in calificaciones.items():
    print(f"{estudiante}: {cal}")
    if nota_mayor<cal:
        estudiant=estudiante
        nota_mayor=cal
print("\nUsando un for para hallar la nota maxima: \n")
print(f' El estudiante con la mayor nota es {estudiant} y su calificacion es de {nota_mayor}.\n')
print("Usando la funcion max para hallar la nota maxima: \n")
nombre_max = max(calificaciones, key=calificaciones.get) 
print(f' El estudiante con la mayor nota es {nombre_max} y su calificacion es de {calificaciones[nombre_max]}.')