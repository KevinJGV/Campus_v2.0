# Dado  el  nombre  y  salario  de  un  empleado,  calcular  el 
# subsidio de transporte, teniendo en cuenta  que  si el 
# salario  es  menor  o  igual  a  $1.200.000  entonces  tiene 
# derecho a un subsidio de transporte por valor de 
# $120.000, de lo contrario no tiene derecho al subsidio de 
# transporte.  Se debe visualizar el nombre, salario y 
# subsidio de transporte 

def int_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            if arg <= 0:
                print("Su salario debe ser mayor a 0.")
            else:
                return arg
        except ValueError:
            print("Su entrada debe ser un numero entero.")

usuario = input("Nombre del empleado: ").strip()
salario = int_input_checker("Salario del empleado (Sin simbolos): ")

if salario <= 1_200_000:
    print(f"USUARIO: {usuario}\nSALARIO: ${salario}\nBONO POR POBREZA: $120.000")
else:
    print(f"USUARIO: {usuario}\nSALARIO: ${salario}\nBONO POR POBREZA: No aplíca.")