# PARTE 4: Combinación de Estructuras
estudiantes = { "Juan": 5.0,"Ana": 4.2,"Luis": 4.5}
n=int(input("Cuantos estudiantes vas a procesar: "))
x=1
while x<=n:
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    if nombre in estudiantes:
        estudiantes[nombre] = calificacion 
        print(f"La calificación de {nombre} ha sido actualizada.")
    else:
        estudiantes[nombre] = calificacion  
        print(f"{nombre} ha sido agregado con una calificación de {calificacion}.")
    x+=1

print("\nListado de estudiantes y calificaciones:")
for estudiante, cal in estudiantes.items():
    print(f"{estudiante}: {cal}")

