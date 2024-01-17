print("Bienvenido a calculando")
num1 = int(input("Introduce un primer número: "))
num2 = int(input("Introduce un segundo número: "))
print("De entre estas operaciones:")
print("1\. Suma")
print("2\. Resta")
print("3\. Multiplicación")
print("4\. División")
operacion = int(input("¿Que operacion deseas realizar? Digita el numero (1, 2, 3, o 4): "))
if operacion == 1:
 resultado = num1 + num2
 print(f"El resultado de x operacion es: {resultado}")
elif operacion == 2:
 resultado = num1 - num2
 print(f"El resultado de x operacion es: {resultado}")
elif operacion == 3:
 resultado = num1 * num2
 print(f"El resultado de x operacion es: {resultado}")
elif operacion == 4:
 resultado = num1 / num2
 print(f"El resultado de x operacion es: {resultado}")
else:
 print("No se eligio una opcion valida")