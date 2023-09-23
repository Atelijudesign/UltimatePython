# Ingreso de datos por el usuario
n1 = float(input('Ingresa el primer numero: '))
n2 = float(input('Ingresa el segundo numero: '))

# Operaciones aritmeticas

suma = n1 + n2
division = n1 / n2
multiplicacion = n1 * n2
resta = n1 - n2

# Output - Mensaje de salida

mensaje = f"""
1- La suma es {suma}
2- La resta es {resta}
3- La division es {division}
4- La multiplicacion es {multiplicacion}
"""

print("--- Operaciones Aritmeticas ---")
print(mensaje)
