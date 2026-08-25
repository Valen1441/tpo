#------------------------ CALIFICAIONES ---------------------
def busqueda_secuencial(matriz, columna, dato):
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

#------------------ ALTAS ESTUDIANTES / MATERIAS ---------------------
def altas_estudiantes_materias(matriz, titulo):
    print()
    print(f" == ALTAS {titulo} ==")

    #Pedir nombre del estudiante/materia
    if titulo == "ESTUDIANTES":
        nombre = input("Ingrese el nombre del nuevo estudiante: ").title()
    else:
        nombre = input("Ingrese el nombre de la nueva materia: ").title()
    
    
    #Pedir edad/cuatrimestre
    if titulo == "ESTUDIANTES":
        edad_cuat = int(input("Ingrese la edad del nuevo estudiante: "))
        while edad_cuat < 17 or edad_cuat > 100:
            print("Edad invalida: rango perimitido de 17 a 100 años")
            edad_cuat = int(input("Ingrese de nuevo la edad del estudiante: "))
    else:
        edad_cuat = int(input("Ingrese el cuatrimestre de la nueva materia"))
        while edad_cuat < 1 or edad_cuat > 2:
            print("Cuatimestre invalido: rango perimitido de 1 a 2")
            edad_cuat = int(input("Ingrese de nuevo el cuatrimestre de la materia: "))


    #Pedir año de cursada / carga horaria
    if titulo == "ESTUDIANTES":
        año_horaria = int(input("Ingrese el año de cursada del nuevo estudiante: "))
        while año_horaria < 1 or año_horaria > 9:
            print("Año de cursada invalido: rango perimitido de 1 a 9")
            año_horaria = int(input("Ingrese de nuevo el año de cursada del estudiante: "))
    else:
        año_horaria = int(input("Ingrese la carga horaria de la nueva materia"))
        while año_horaria < 1 or año_horaria > 12:
            print("Carga horaria invalida: rango perimitido de 1 a 12 horas")
            año_horaria = int(input("Ingrese de nuevo la carga horaria de la materia: "))

        
    codigo = matriz[len(matriz) - 1][0] + 1

    #Agregar
    matriz.append([codigo, nombre, edad_cuat, año_horaria])

    if titulo == "ESTUDIANTES":
        print(f"Estudiante {codigo} agreagado.")
    else: 
        print(f"Materia {codigo} agreagada.")
    

#------------------ BAJAS ESTUDIANTES / MATERIAS ---------------------
def bajas_estudiantes_materias(matriz, titulo):
    print()
    print(f" == BAJAS {titulo} ==")

    if titulo == "ESTUDIANTES":
        codigo = int(input("Ingrese el código del estudiante a eliminar (Formato: 100): "))
    else:
        codigo = int(input("Ingrese el código de la materia a eliminar (Formato: 100): "))
    
    registrado = busqueda_secuencial(matriz, 0, codigo)
            
    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        if titulo == "ESTUDIANTES":
            codigo = int(input("Ingrese el código del estudiante a eliminar (Formato: 100): "))
        else:
            codigo = int(input("Ingrese el código de la materia a eliminar (Formato: 100): "))
    
        registrado = busqueda_secuencial(matriz, 0, codigo)
                    

    matriz.pop(registrado)
    
    if titulo == "ESTUDIANTES":
        print(f"Estudiante {codigo} eliminado.")
    else: 
        print(f"Materia {codigo} agreagada.")
    

#------------------ MODIFICACION ESTUDIANTES / MATERIAS ---------------------
def modificar_estudiantes_materias(matriz, titulo):
    print()
    print(f" == MODIFICACIÓN {titulo} ==")
    
    #Pedir el codigo a modificar
    if titulo == "ESTUDIANTES":
        codigo = int(input("Ingrese el código del estudiante a modificar (Formato: 100): "))
    else:
        codigo = int(input("Ingrese el código de la materia a modificar (Formato: 100): "))
    
    modificar = busqueda_secuencial(matriz, 0, codigo)

    while modificar == -1:
        print("ERROR: Ese código no está registrado")
        
        if titulo == "ESTUDIANTES":
            codigo = int(input("Ingrese el código del estudiante a modificar (Formato: 100): "))
        else:
            codigo = int(input("Ingrese el código de la materia a modificar (Formato: 100): "))
    
        modificar = busqueda_secuencial(matriz, 0, codigo)
                
                
#Pedir nombre del estudiante/materia
    if titulo == "ESTUDIANTES":
        nombre = input("Ingrese el nombre del estudiante: ").title()
    else:
        nombre = input("Ingrese el nombre de la materia: ").title()
    
    
#Pedir edad/cuatrimestre
    if titulo == "ESTUDIANTES":
        edad_cuat = int(input("Ingrese la edad del estudiante: "))
        while edad_cuat < 17 or edad_cuat > 100:
            print("Edad invalida: rango perimitido de 17 a 100 años")
            edad_cuat = int(input("Ingrese de nuevo la edad del estudiante: "))
    else:
        edad_cuat = int(input("Ingrese el cuatrimestre de la materia"))
        while edad_cuat < 1 or edad_cuat > 2:
            print("Cuatimestre invalido: rango perimitido de 1 a 2")
            edad_cuat = int(input("Ingrese de nuevo el cuatrimestre de la materia: "))


    #Pedir año de cursada / carga horaria
    if titulo == "ESTUDIANTES":
        año_horaria = int(input("Ingrese el año de cursada del estudiante: "))
        while año_horaria < 1 or año_horaria > 9:
            print("Año de cursada invalido: rango perimitido de 1 a 9")
            año_horaria = int(input("Ingrese de nuevo el año de cursada del estudiante: "))
    else:
        año_horaria = int(input("Ingrese la carga horaria de la materia"))
        while año_horaria < 1 or año_horaria > 12:
            print("Carga horaria invalida: rango perimitido de 1 a 12 horas")
            año_horaria = int(input("Ingrese de nuevo la carga horaria de la materia: "))
        

    #Modificar
    matriz[modificar][0] = codigo
    matriz[modificar][1] = nombre
    matriz[modificar][2] = edad_cuat
    matriz[modificar][3] = año_horaria

    if titulo == "ESTUDIANTES":
        print(f"Estudiante {codigo} modificado.")
    else: 
        print(f"Materia {codigo} modificada.")
        
        


def clasificar_nota(nota):
    if nota >= 8:
        cadena = f"{AZUL}Promocionada{RESET}"
    elif nota >= 4:
        cadena = f"{VERDE}Aprobada{RESET}"
    else:
        cadena = f"{ROJO}Desaprobada{RESET}"
    return cadena
    
def imprimir_matriz(matriz, titulo):

    if titulo == "ESTUDIANTES":
        print("="*55)
        print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^55}{RESET}')
        print("="*55)
        print(f"{BOLD}{'Legajo':<13}{'Nombre':<16}{'Edad':<13}{'Año Cursada':<21}{RESET}")
        print("-" * 55)
    else:
        print("="*65)
        print(f'{BOLD}{MAGENTA}{"MATERIAS":^65}{RESET}')
        print("="*65)
        print(f"{BOLD}{'Id Materia':<16}{'Nombre':<16}{'Cuatrimestre':<17}{'Carga Horaria':<21}{RESET}")
        print("-" * 65)

    # Datos
    for i in range(len(matriz)):
        codigo = matriz[i][0]
        nombre = matriz[i][1]
        edad_cuat = matriz[i][2]
        año_horaria = matriz[i][3]

        if titulo == "ESTUDIANTES":
            print(f"{codigo:<13}{nombre:<16}{edad_cuat:^4}{año_horaria:>15}")
        else:
            print(f"{codigo:<16}{nombre:<16}{edad_cuat:^12}{año_horaria:>12}")



def ordenar_matriz(matriz, columna, reversa):
    if reversa == 0: 
        matriz.sort(key=lambda fila: fila[columna])
    else:
        matriz.sort(key=lambda fila: fila[columna], reverse=True)



def mostrar_estudiantes_materias(matriz, titulo):
    columna = int(input("Ingrese una columna: "))
    reversa = int(input("1: para ordenar de mayor a menor, 0: viceversa: "))
    ordenar_matriz(matriz, columna, reversa)
    imprimir_matriz(matriz, titulo)



# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"


