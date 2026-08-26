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
    estudiante = int(input("Ingrese el legajo del estudiante a calificar (Formato: 100): "))
    
    registrado = busqueda_secuencial(estudiantes, 0, estudiante)
            
    while registrado == -1:
        print("ERROR: Ese legajo no está registrado.")
        
        estudiante = int(input("Ingrese de nuevo el legajo del estudiante a calificar (Formato: 100): "))
    
        registrado = busqueda_secuencial(estudiantes, 0, estudiante)
    
    
    #Pedir id de la materia
    materia = int(input("Ingrese el codigo de la materia (Formato: 100): "))
    
    registrado = busqueda_secuencial(materias, 0, materia)
            
    while registrado == -1:
        print("ERROR: Ese codigo de materia no está registrado.")
        
        materia = int(input("Ingrese de nuevo el codigo de la materia (Formato: 100): "))
    
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

    # ==============================
    # REPORTE / BOLETÍN DEL ALUMNO
    # ==============================

    # Buscar nombre del alumno
    posicion_estudiante = busqueda_secuencial(estudiantes, 0, estudiante)
    nombre_alumno = estudiantes[posicion_estudiante][1]

    print()
    print("========================================")
    print("              BOLETÍN")
    print("========================================")
    print("Alumno:", nombre_alumno)
    print("Legajo:", estudiante)
    print("----------------------------------------")

    for registro in notas:
        if registro[2] == estudiante:

            nota_alumno = registro[1]
            codigo_materia = registro[3]

            # Buscar la materia
            posicion_materia = busqueda_secuencial(materias, 0, codigo_materia)
            nombre_materia = materias[posicion_materia][1]

            if nota_alumno >= 8:
                resultado = "PROMOCIONA"
            elif nota_alumno >= 4:
                resultado = "APRUEBA"
            else:
                resultado = "DESAPRUEBA"

            print("Materia:", nombre_materia)
            print("Nota:", nota_alumno)
            print("Resultado:", resultado)
            print("----------------------------------------")
    

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

    registrado = busqueda_secuencial(estudiantes, 1, legajo)

    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        legajo = int(input("Ingrese el nuevo legajo del estudiante de la nota (Formato: 100): "))

        registrado = busqueda_secuencial(estudiantes, 1, legajo)
        
    #Pedir el nuevo codigo de materia
    materia = input("Ingrese el nuevo id de la materia de la nota (Formato: 100): ")

    registrado = busqueda_secuencial(materias, 1, materia)

    while registrado == -1:
        print("ERROR: Ese código no está registrado")
        
        materia = int(input("Ingrese otra vez el nuevo id de la materia de la nota (Formato: 100): "))

        registrado = busqueda_secuencial(materias, 1, materia)
    
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
        
        