import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()


def mostrar_calificaciones(notas, estudiantes, materias):

    try:
        arch = open(notas, "rt", encoding="UTF-8")
    except OSError as error:
        print(f'No se pudo leer el archivo {notas}: {error}')
    else:
        nombres_est = utilidades.crear_diccionario_json(estudiantes, "legajo", "nombre")
        nombres_mat = utilidades.crear_diccionario_plano(materias, 0, 1)
        print("="*80)
        print(f'{BOLD}{MAGENTA}{"CALIFICACIONES":^80}{RESET}')
        print("="*80)
        print(f"{BOLD}{'ID Nota':<7}{'Nota':^16}{'Estudiante':<21}{'Materia':<15}{'Condición':^24}{RESET}")
        print("-" * 80)
        for linea in arch:
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            nota = int(datos[1])
            legajo_est = int(datos[2])
            estudiante = utilidades.devolver_dato_json(estudiantes, "legajo", legajo_est, "nombre")
            if len(estudiante) > 15:
                estudiante = estudiante[:12] + "..."

            id_materia = int(datos[3])
            materia = utilidades.devolver_dato_plano(materias, 0, id_materia, 1)
            if len(materia) > 15:
                materia = materia[:12] + "..."

            condicion = utilidades.clasificar_nota(nota)
            print(f"{codigo:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")
            linea = arch.readline()
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)