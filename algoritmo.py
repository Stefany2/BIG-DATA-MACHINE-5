#Desarrollar un algoritmo donde me permita ingresar 4 números y 
# luego los ordene de menor a mayor.

# Pedir al usuario que ingrese 4 números
numeros = []
for i in range(4):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Ordenar los números de menor a mayor
numeros_ordenados = sorted(numeros)

# Mostrar el resultado
print("Los números ordenados de menor a mayor son:")
for numero in numeros_ordenados:
    print(numero)
