import numpy as np

# Usando Numpy. Desarrollar una matriz que me diga de 10 datos donde se encuentra el numero "0"

# Crear una matriz de 10 elementos (puede incluir ceros)
datos = np.array([int(input(f"Ingrese el número {i + 1}: ")) for i in range(10)])

# Encontrar las posiciones donde se encuentra el número "0"
posiciones_cero = np.where(datos == 0)[0]

# Mostrar el resultado
if posiciones_cero.size > 0:
    print("El número 0 se encuentra en las posiciones:", posiciones_cero)
else:
    print("El número 0 no se encuentra en los datos.")




