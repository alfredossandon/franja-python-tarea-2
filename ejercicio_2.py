# Ejercicio 2: Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.

#AREA DEL CIRCULO
import math

radio = float(input("Ingrese el valor del radio de su circulo: "))
area = math.pi * (radio**2)
resultado = area
print(f"El resultado del area de su circulo es {resultado} ")


#VOLUMEN DEL CILINDRO (AREA * h)
alturah = float(input("Ingrese la altura de su cilindro: "))
resultado = area * alturah 
print(f"El resultado del volumen del cilindro es {resultado}")