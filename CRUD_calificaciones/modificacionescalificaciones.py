import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def modificar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita una calificación existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN CALIFICACIONES{RESET} ====================")

    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo_modif = utilidades.leerentero("Ingrese el código de la nota a modificar (Formato: 100): ")
            nota_modificar = utilidades.devolver_dato_plano(notas, 0, codigo_modif)
            assert nota_modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")
                
                
    # Pedir el nuevo legajo
    legajo, materia, nota = utilidades.pedir_datos_calificacion(estudiantes, materias)
        

    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3
    
    nueva_linea = f'{codigo_modif};{nota};{legajo};{materia};{condicion}\n'

    if utilidades.actualizar_archivo_plano(notas, 0, codigo_modif, nueva_linea):
        print(f"Nota {codigo_modif} modificada.")