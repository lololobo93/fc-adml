debug = True #Cambien este valor a False para pedir los datos al usuario

#Arreglo de entrenamiento
text = "6,3,9,5,1,7,1"

if not debug:
    text = input("Ingrese una secuencia de valores naturales separados por coma: ")

#Convertimos la cadena de caracteres en una lista
values = [int(i) for i in text.split(',')]

# Coloquen aquí su algoritmo de acomodo para acomodar la variable values

print(values)