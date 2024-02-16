def int_input_checker(msj):
    while True:
        try:
            arg = int(input(msj))
            if arg < 0 or arg > 100:
                print("Error. Ingrese un valor entre 0 a 100.")
            else:
                return arg
        except ValueError:
            print("Su entrada debe ser un numero entero.")
            
def str_input_checker(msj):
    while True:
        try:
            arg = input(msj).strip()
            if len(arg) > 0 :
                return arg                
        except ValueError:
            print("Error. Intente de nuevo.")
            
estudiante = str_input_checker("Nombre del estudiante: ")
print(f"\nBienvenido {estudiante}, porfavor suministre su nota para la conversión")
nota = int_input_checker("")

if nota >= 90:
    print(f"Resultado de conversion para el estudiante '{estudiante}':\nNota Cuantitativa: {nota}\nNota Cualitativa: A\nResultado: Excelente")
elif nota >= 80:
    print(f"Resultado de conversion para el estudiante '{estudiante}':\nNota Cuantitativa: {nota}\nNota Cualitativa: B\nResultado: Buena")
elif nota >= 60:
    print(f"Resultado de conversion para el estudiante '{estudiante}':\nNota Cuantitativa: {nota}\nNota Cualitativa: C\nResultado: Mediocre")
elif nota >= 0:
    print(f"Resultado de conversion para el estudiante '{estudiante}':\nNota Cuantitativa: {nota}\nNota Cualitativa: D\nResultado: Reprovado")

