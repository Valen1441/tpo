import utilidades
import os

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def bajas_calificaciones(notas):
    '''
    pre: recibe la matriz de calificaciones.
    pos: solicita el código de una calificación y elimina el registro correspondiente.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS CALIFICACIONES{RESET} ====================")

    # Pedir el codigo a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la nota a eliminar (Formato: 100): ")
            registrado = utilidades.devolver_dato_plano(notas, 0, codigo_baja)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

    if utilidades.actualizar_archivo_plano(notas, 0, codigo_baja):
        print(f"Nota {codigo_baja} eliminada.")