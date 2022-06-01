# Ejercicio 3: Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario 
# la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $3.500 y si es mayor de 18 años, $8.000.

print("¡¡¡¡SALA DE JUEGOS PARA NIÑOS Y MAYORES!!!!")

edad = int(input("Ingrese edad del cliente: "))
if edad < 4:
    print("El niño puede ingresar gratis a la sala de juegos")
elif edad >= 4:
    print("El cliente debe pagar $ 3.500 Pesos")
elif edad > 18:
    print("El cliente debe pagar $ 8.000 pesos ")
print("!MUCHAS GRACIAS POR OCUPAR NUESTRO SISTEMA¡")