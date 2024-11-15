#Desarrollar un algoritmo donde me permita ingresar 5 números, donde me permita 
# sacar el promedio del primer y ultimo numero.

# Ingresar 4 números
numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(5)]

# Calcular y mostrar el promedio del primer y último número
promedio = (numeros[0] + numeros[-1]) / 2
print("El promedio del primer y último número es:", promedio)







