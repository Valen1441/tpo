#------------------------ CALIFICAIONES ---------------------
def busqueda_secuencial(matriz, columna, dato):
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

#------------------ ALTAS CALIFICACIONES ---------------------
def altas_calificaciones(notas, estudiantes, materias):
    print()
    print(" == ALTAS CALIFICACIONES ==")

    #Pedir legajo del estudiante 
    estudiante = int(input("Ingrese el legajo del estudiante a calificar: "))
    
    registrado = busqueda_secuencial(estudiantes, 0, estudiante)
            
    while registrado == -1:
        print("ERROR: Ese legajo no está registrado.")
        
        estudiante = int(input("Ingrese de nuevo el legajo del estudiante a calificar: "))
    
        registrado = busqueda_secuencial(estudiantes, 0, estudiante)
    
    
    #Pedir id de la materia
    materia = int(input("Ingrese el codigo de la materia: "))
    
    registrado = busqueda_secuencial(materias, 0, materia)
            
    while registrado == -1:
        print("ERROR: Ese codigo de materia no está registrado.")
        
        materia = int(input("Ingrese de nuevo el codigo de la materia: "))
    
        registrado = busqueda_secuencial(materias, 0, materia)
        
    
    #Pedir la nota
    nota = int(input("Ingrese la nota: "))    
    
    while nota <= 0 or nota > 10:
        print("ERROR: La nota debe ser mayor a 0 y menor o igual a 10.")
            
        nota = int(input("Ingrese de nuevo la nota: "))

        
    codigo = notas[len(notas) - 1][0] + 1
    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    #Agregar
    notas.append([codigo, nota, estudiante, materia, condicion])

    print("Nota",codigo,"agreagada.")
    

#------------------ BAJAS CALIFICACIONES ---------------------
def bajas_calificaciones(notas):
    print()
    print(" == BAJAS CALIFICACIONES ==")
    
    codigo = int(input("Ingrese el código de la nota a eliminar (Formato: 100): "))
    
    registrado = busqueda_secuencial(notas, 0, codigo)
            
    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        codigo = int(input("Ingrese de nuevo el código de la nota a eliminar (Formato: 100): "))
    
        registrado = busqueda_secuencial(notas, 0, codigo)
                    

    notas.pop(registrado)
    
    print("Nota",codigo,"eliminado.")
    

#------------------ MODIFICACION CALIFICACIONES ---------------------
def modificar_calificaciones(notas, estudiantes, materias):
    print()
    print(" == MODIFICACIÓN CALIFICACIONES ==")
    
    #Pedir el codigo a modificar
    codigo = int(input("Ingrese el código de la nota a modificar (Formato: 100): "))
    
    nota_modificar = busqueda_secuencial(notas, 0, codigo)

    while nota_modificar == -1:
        print("ERROR: Ese código no está registrado")
        
        codigo = int(input("Ingrese el código de la nota a modificar (Formato: 100): "))
    
        nota_modificar = busqueda_secuencial(notas, 0, codigo)
                
                
    #Pedir el nuevo legajo
    legajo = int(input("Ingrese el nuevo legajo del estudiante de la nota (Formato: 100): "))

    registrado = busqueda_secuencial(estudiantes, 0, legajo)

    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        legajo = int(input("Ingrese el nuevo legajo del estudiante de la nota (Formato: 100): "))

        registrado = busqueda_secuencial(estudiantes, 0, legajo)
        
    #Pedir el nuevo codigo de materia
    materia = int(input("Ingrese el nuevo id de la materia de la nota (Formato: 100): "))

    registrado = busqueda_secuencial(materias, 0, materia)

    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        materia = int(input("Ingrese otra vez el nuevo id de la materia de la nota (Formato: 100): "))

        registrado = busqueda_secuencial(materias, 0, materia)
    
    #Pedir la nueva nota
    nota = int(input("Ingrese la nueva nota: "))    
    
    while nota <= 0 or nota > 10:
        print("ERROR: La nota debe ser mayor a 0 y menor o igual a 10.")
            
        nota = int(input("Ingrese otra vez la nueva nota: "))
        

    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    #Modificar
    notas[nota_modificar][0] = codigo
    notas[nota_modificar][1] = nota
    notas[nota_modificar][2] = legajo
    notas[nota_modificar][3] = materia
    notas[nota_modificar][4] = condicion
    
    print("Nota",codigo,"modificada.")
        
        




def clasificar_nota(nota):
    if nota >= 8:
        cadena = f"{AZUL}Promocionada{RESET}"
    elif nota >= 4:
        cadena = f"{VERDE}Aprobada{RESET}"
    else:
        cadena = f"{ROJO}Desaprobada{RESET}"
    return cadena
    
def imprimir_calificacion(notas, estudiantes, materias):
    # Encabezado
    print("="*72)
    print(f'{BOLD}{MAGENTA}{"CALIFICACIONES":^72}{RESET}')
    print("="*72)
    print(f"{BOLD}{'ID Nota':<13}{'Nota':<10}{'Estudiante':<17}{'Materia':<21}{'Condición':<17}{RESET}")
    print("-" * 72)

    # Datos
    for i in range(len(notas)):
        id_nota = notas[i][0]
        nota = notas[i][1]

        estudiante = notas[i][2]
        pos = busqueda_secuencial(estudiantes, 0, estudiante)
        estudiante = estudiantes[pos][1]

        materia = notas[i][3]
        pos = busqueda_secuencial(materias, 0, materia)
        materia = materias[pos][1]
        
        condicion = clasificar_nota(nota)
        print(f"{id_nota:^7}{nota:^16}{estudiante:<17}{materia:<19}{condicion:^25}")


def ordenar_matriz(matriz, columna, reversa):
    if reversa == 0: 
        matriz.sort(key=lambda fila: fila[columna])
    else:
        matriz.sort(key=lambda fila: fila[columna], reverse=True)

    


# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"



def mostrar_calificaciones(notas, estudiantes, materias):
    columna = int(input("Ingrese el número de la columna para ordenar (1-5): ")) - 1
    while columna < 0 or columna > 3:
        print(f"{ROJO}Número fuera de rango, la matriz posee 5 columnas{RESET}")
        columna = int(input("Ingrese de nuevo el número de la columna para ordenar (1-5): ")) - 1
    
    reversa = int(input("Ingrese 0 = ascendente, 1 = descendente: "))
    while reversa < 0 or reversa > 1:
            print(f"{ROJO}Número inválido, rango valido de 0 a 1{RESET}")
            reversa = int(input("Ingrese 0 = ascendente, 1 = descendente: ")) - 1

    ordenar_matriz(notas, columna, reversa)
    imprimir_calificacion(notas, estudiantes, materias)