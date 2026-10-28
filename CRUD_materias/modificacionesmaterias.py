import utilidades
import os

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
            codigo_modif = utilidades.leerentero("Ingrese el código de la materia a modificar (Formato: 100): ")
            modificar = utilidades.encontrar_dato(materias, 0, codigo_modif)
            assert modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

                
    # Pedir nombre de la materia
    nombre = input("Ingrese el nombre de la materia: ").title()
    
    
    # Pedir el cuatrimestre
    while True:
        try:
            cuatrimestre = utilidades.leerentero("Ingrese el cuatrimestre de la nueva materia (1-2): ")
            assert cuatrimestre >= 1 and cuatrimestre <= 2
            break
        except AssertionError:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            print("Intente nuevamente.")


    # Pedir año de la materia
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de la nueva materia (1-5): ")
            assert anio >= 1 and anio <= 5
            break
        except AssertionError:
            print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
            print("Intente nuevamente.")


    # Pedir carga horaria 
    while True:
        try:
            horaria = utilidades.leerentero("Ingrese la carga horaria de la nueva materia (1-12): ")
            assert horaria >= 1 and horaria <= 12
            break
        except AssertionError:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            print("Intente nuevamente.")

    temp = "temp.txt"
    encontrado = False

    try:
        arch = open(materias, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(";")
            codigo = int(datos[0])

            if codigo == codigo_modif:
                encontrado = True

                nueva_linea = f'{codigo_modif};{nombre};{cuatrimestre};{anio};{horaria}\n'
                aux.write(nueva_linea)
                print(f"Materia {codigo_modif} modificada.")
            else:
                aux.write(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove(materias)
            os.rename(temp, materias)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró la materia {codigo_modif}.")