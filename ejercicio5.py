import math

# Solicitar al usuario el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el área lateral del cilindro
area_lateral = 2 * math.pi * radio * altura

# Calcular el área total del cilindro
area_total = 2 * math.pi * radio * (altura + radio)

# Calcular el volumen del cilindro
volumen = math.pi * radio ** 2 * altura

# Imprimir el área lateral, área total y volumen del cilindro
print(f"El área lateral del cilindro es: {area_lateral:.2f}")
print(f"El área total del cilindro es: {area_total:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")
