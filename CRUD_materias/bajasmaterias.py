import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def bajas_materias(materias, notas):
    '''
    pre: recibe la matriz de materias y la de notas.
    pos: solicita el código de una materia y elimina el registro correspondiente, 
         siempre que exista y no tenga una calificación registrada.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS MATERIAS{RESET} ====================")

    # Pedir el código a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la materia a eliminar (Formato: 100) (0 para cancelar): ")
            if codigo_baja == 0:
                print("Operación cancelada.")
                return
            esta_en_calificaciones = utilidades.devolver_dato_plano(notas, 3, codigo_baja)
            registrado = utilidades.devolver_dato_plano(materias, 0, codigo_baja)
            assert esta_en_calificaciones == -1
            assert registrado != -1
            break
        except AssertionError:
            if registrado == -1:
                print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            else:
                print(f"{ROJO}ERROR: Esa materia tiene una calificación registrada, no se puede eliminar{RESET}")
            print("Intente nuevamente.")

        if utilidades.actualizar_archivo_plano(materias, 0, codigo_baja):
            print(f"Materia {codigo_baja} eliminada correctamente.")