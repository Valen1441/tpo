import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def modificar_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: solicita una materia existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN MATERIAS{RESET} ====================")
    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo_modif = utilidades.leerentero("Ingrese el código de la materia a modificar (Formato: 100) (0 para cancelar): ")
            if codigo_modif == 0:
                print("Operación cancelada.")
                return
            modificar = utilidades.devolver_dato_plano(materias, 0, codigo_modif)
            assert modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

                
    # Pedir nombre de la materia
    nombre, cuatrimestre, anio, horaria = utilidades.pedir_datos_materia()


    nueva_linea = f'{codigo_modif};{nombre};{cuatrimestre};{anio};{horaria}\n'

    if utilidades.actualizar_archivo_plano(materias, 0, codigo_modif, nueva_linea):
        print(f"Materia {codigo_modif} modificada.")