# Escribe un programa en  Python que determine si un año 
# ingresado  por  el  usuario  es  bisiesto  o  no.  Un   año  bisiesto  es 
# aquel que es divisible entre 4, excepto aquellos divisibles entre 
# 100 pero no entre 400.
# El programa debe realizar lo siguiente:
# Solicitar al usuario que ingrese un año.
# Verificar si el año cumple con las condiciones para ser bisiesto.
# Mostrar un mensaje indicando si el año es bisiesto o no.

def int_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            return arg
        except ValueError:
            print("Su entrada debe ser un numero entero.")

año = int_input_checker("Evaluador de año bisiesto\nIngrese el año a evaluar: ")
if año % 4 == 0:
    if año % 100 == año % 400:
        print("Este año ES bisiesto")
    else:
        print("Este año NO es bisiesto")
else:
    print("Este año NO es bisiesto")