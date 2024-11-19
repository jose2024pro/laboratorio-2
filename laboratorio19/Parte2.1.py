#PARTE 2.1 - Coordenadas

cant1 = 0 #puntos en cuadrante 1
cant2 = 0 #puntos en cuadrante 2
cant3 = 0 #puntos en cuadrante 3
cant4 = 0 #puntos en cuadrante 4

n = int(input("Cantidad de puntos a digitar: "))

for f in range(n):
    x = int(input("Ingrese coordenada en x: "))
    y = int(input("ingrese coordenada en y: "))
    print(f'Punto ({x},{y})')
    if x>0 and y>0:
        cant1+= 1
    elif x<0 and y>0:
        cant2 += 1
    elif x<0 and y<0:
        cant3 += 1
    else:
        cant4 += 1

print(f' hay {cant1} de puntos en el cuadrante 1')
print(f' hay {cant2} de puntos en el cuadrante 2')
print(f' hay {cant3} de puntos en el cuadrante 3')
print(f' hay {cant4} de puntos en el cuadrante 4')