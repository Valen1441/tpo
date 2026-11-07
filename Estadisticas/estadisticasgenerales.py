import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()


def resumen_general(arch_notas):
    '''
    pre: recibe la ruta del archivo de notas.
    pos: lee el archivo una sola vez, línea por línea, y muestra un resumen estadístico general:
         total de notas, promedio general, nota más alta, nota más baja y la cantidad y el
         porcentaje de notas aprobadas, promocionadas y desaprobadas. Si no hay notas, o el
         archivo no se puede leer, lo informa.
    '''
    total = 0
    suma = 0
    maxima = -1
    minima = -1
    por_condicion = {1: 0, 2: 0, 3: 0}   # 1 = aprobada, 2 = promocionada, 3 = desaprobada

    try:
        with open(arch_notas, "rt", encoding="UTF-8") as notas:
            for linea in notas:
                datos = linea.strip().split(";")
                nota = int(datos[1])
                total += 1
                suma += nota
                if maxima == -1 or nota > maxima:
                    maxima = nota
                if minima == -1 or nota < minima:
                    minima = nota
                por_condicion[int(datos[4])] += 1
    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_notas}.{RESET}")
    except (OSError, ValueError, KeyError) as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_notas}: {error}{RESET}")
    else:
        if total == 0:
            print("No hay notas registradas.")
        else:
            print()
            print("=" * 50)
            print(f'{BOLD}{MAGENTA}{"RESUMEN GENERAL DE CALIFICACIONES":^50}{RESET}')
            print("=" * 50)
            print(f"Total de notas registradas: {total}")
            print(f"Promedio general: {suma / total:.1f}")
            print(f"Nota más alta: {maxima}")
            print(f"Nota más baja: {minima}")
            print("-" * 50)
            print(f"{VERDE}Aprobadas:{RESET}     {por_condicion[1]:>4}  ({por_condicion[1] / total * 100:.1f}%)")
            print(f"{AZUL}Promocionadas:{RESET} {por_condicion[2]:>4}  ({por_condicion[2] / total * 100:.1f}%)")
            print(f"{ROJO}Desaprobadas:{RESET}  {por_condicion[3]:>4}  ({por_condicion[3] / total * 100:.1f}%)")