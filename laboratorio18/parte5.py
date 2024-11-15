#Se crea el diccionario
dicci = {"Nombre": "Jose Lopez", "Edad": "23", "Ciudad": "Valledupar", "Profesión": "Estudiante"}
print(dicci)
#Se imprime solo un clave-valor
print(dicci["Nombre"])
#Se modifica la Edad
dicci["Edad"] = 24
print(dicci)
#Se agrega nuevos clave-valor al diccionario con update tambien 
dicci.update({"Estado Civil": "Soltero"})
dicci["Sexo"] ="M"

print(dicci)
#Se elimina un clave-valor
del dicci["Sexo"]
print(dicci)