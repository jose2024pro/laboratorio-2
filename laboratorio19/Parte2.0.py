# PARTE 2 - Empresa con n empleados, bucle while, contadores y condiciones
nEmpleado = int(input("¿Cuántos empleados tiene la empresa? "))
x = 1
cont1 = 0  #contador de sueldos entre 1000000 y 3000000
cont2 = 0  #contador de sueldos 3000000 en adelante
costos = 0  #gastos en costos de sueldos en la empresa

while x <= nEmpleado:
    sueldo = float(input(f"Ingrese el sueldo del empleado {x}: "))
    if 1000000 > sueldo or sueldo>5000000:
        print("Salario no valido")
        continue
    if 1000000 <= sueldo <= 3000000:
        cont1 += 1
    elif sueldo > 3000000:
        cont2 += 1
    costos += sueldo
    x += 1

print(f"Empleados que ganan entre $1,000,000 y $3,000,000: {cont1}")
print(f"Empleados que ganan más de $3,000,000: {cont2}")
print(f"Total de gastos de la empresa en costos de sueldos: ${costos:.2f}")
