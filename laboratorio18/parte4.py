lista=[]
print(F'lista vacia = {lista}')
lista =[1,"jose", True, 3.14]
print(f'Lista inicial = {lista}')
lista[0] = 100
print(f'Lista con atributo 0 cambiado = {lista}')
lista.append("maria")
print(f'Lista con atributo nuevo "maria" = {lista}')
lista.insert(2, 300)
print(f'Lista con atributo nuevo 300 en posicion 2 = {lista}')
lista.pop()
print(f'Lista con atributo ultimo eliminado = {lista}')
lista.remove(True)
print(f'Lista con atributo especifico True eliminado = {lista}')