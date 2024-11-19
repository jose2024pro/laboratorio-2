#PARTE 1 - par e inpar
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


#PARTE 1.2 - Numeros de digitos de un numero max 3
numero2 = int(input("Ingrese un número entre 1 y 999: "))

if 1 <= numero2 <= 9:
    print(f"El número {numero2} tiene 1 dígito.")
elif 10 <= numero2 <= 99:
    print(f"El número {numero2} tiene 2 dígitos.")
elif 100 <= numero2 <= 999:
    print(f"El número {numero2} tiene 3 dígitos.")
else:
    print("Número fuera del rango permitido.")
 