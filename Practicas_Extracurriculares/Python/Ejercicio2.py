def int_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            if arg <= 0:
                print("Ingrese un número válido.")
            else:
                return arg
        except ValueError:
            print("Su entrada debe ser un numero entero.")
        
entrada = int_input_checker("Segundos a calcular: ")
horas = entrada // 3600
segundos_restantes = entrada % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60
print(f"Salida:\nHora(s): {horas}\nMinutos: {minutos}\nSegundos: {segundos}")