# Diseñe y escriba un programa que solicite tres números enteros 
# (pueden ser positivos o negativos) y como salida los muestre en  
# orden de mayor a menor.

def int_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            return arg
        except ValueError:
            print("Su entrada debe ser un numero entero.")
def op_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            if arg < 0 or arg > 1:
                print("Error. Ingrese una opción correcta.")
            elif arg == 0:
                print("Configuracion de ordenamiento = ASCENDENTE")
                return arg
            else:
                print("Configuracion de ordenamiento = DESCENDENTE")
                return arg
        except ValueError:
            print("Error.")
            
print("Algoritmo ordenador de 3 numeros")
num1 = int_input_checker("Digite el primer numero: ")
num2 = int_input_checker("Digite el segundo numero: ")
num3 = int_input_checker("Digite el tercer numero: ")
op = op_input_checker("Ordenar ascendentemente [0]\nOrdenar descendentemente[1]\n")

if op == 1:
    if num1 > num2 and num1 > num3:
        print(f"Valor 1: {num1}")
        if num2 > num3:
            print(f"Valor 2: {num2}")
            print(f"Valor 3: {num3}")
        else:
            print(f"Valor 2: {num3}")
            print(f"Valor 3: {num2}")
    elif num2 > num1 and num2 > num3:
        print(f"Valor 1: {num2}")
        if num1 > num3:
            print(f"Valor 2: {num1}")
            print(f"Valor 3: {num3}")
        else:
            print(f"Valor 2: {num3}")
            print(f"Valor 3: {num1}")
    else:
        print(f"Valor 1: {num3}")
        if num1 > num2:
            print(f"Valor 2: {num1}")
            print(f"Valor 3: {num2}")
        else:
            print(f"Valor 2: {num2}")
            print(f"Valor 3: {num1}")
else:
    if num1 < num2 and num1 < num3:
        print(f"Valor 1: {num1}")
        if num2 < num3:
            print(f"Valor 2: {num2}")
            print(f"Valor 3: {num3}")
        else:
            print(f"Valor 2: {num3}")
            print(f"Valor 3: {num2}")
    elif num2 < num1 and num2 < num3:
        print(f"Valor 1: {num2}")
        if num1 < num3:
            print(f"Valor 2: {num1}")
            print(f"Valor 3: {num3}")
        else:
            print(f"Valor 2: {num3}")
            print(f"Valor 3: {num1}")
    else:
        print(f"Valor 1: {num3}")
        if num1 < num2:
            print(f"Valor 2: {num1}")
            print(f"Valor 3: {num2}")
        else:
            print(f"Valor 2: {num2}")
            print(f"Valor 3: {num1}")