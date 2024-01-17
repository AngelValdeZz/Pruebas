print("== Sistema de Operaciones ==")
print("")
print("Opciones a Ejecutar")
print("1 - SUMA")
print("2 - RESTA")
print("3 - MULTIPLICACIÓN")
print("4 - DIVISIÓN")

operacion= int(input("Seleccione una de las opciones: "))

num1= int(input("Ingrese el primer valor: "))
num2= int(input("Ingrese el segundo valor: "))

if operacion == 1:
    resultado = num1 + num2
    print(f"El resultado de la suma de {num1} + {num2} es igual a {resultado}")

elif operacion == 2:
    resultado = num1 - num2
    print(f"El resultado de la resta de {num1} + {num2} es igual a {resultado}")

elif operacion == 3:
    resultado = num1 * num2
    print(f"El resultado de la multiplicación de {num1} + {num2} es igual a {resultado}")

elif operacion == 4:
    resultado = num1 / num2
    print(f"El resultado de la división de {num1} + {num2} es igual a {resultado}")