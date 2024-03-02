# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Sumar los tres números
suma = num1 + num2 + num3

# Calcular el promedio
promedio = suma / 3

# Imprimir el promedio
print(f"El promedio de los tres números es: {promedio:.2f}")
