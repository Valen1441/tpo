import re
#------------------------ ESTUDIANTES Y MATERIAS ---------------------
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
        nombre = input("Ingrese el nombre y apellido del nuevo estudiante: ").title()

        if len(nombre.split()) != 2:
            print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
            nombre = input("Ingrese otra vez el nombre y apellido del nuevo estudiante: ").title()

        nombre = nombre.split()
        nombre = nombre[0] + " " + nombre[1]
    else:
        nombre = input("Ingrese el nombre de la nueva materia: ").title()
    
    
    #Pedir edad/cuatrimestre
    if titulo == "ESTUDIANTES":
        edad_cuat = input("Ingrese la edad del nuevo estudiante: ")

        while edad_cuat.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad_cuat = input("Ingrese otra vez la edad del nuevo estudiante: ")
        edad_cuat = int(edad_cuat)

        while edad_cuat < 17 or edad_cuat > 100:
            print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
            edad_cuat = input("Ingrese otra vez la edad del nuevo estudiante: ")

            while edad_cuat.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                edad_cuat = input("Ingrese otra vez la edad del nuevo estudiante: ")
            edad_cuat = int(edad_cuat)
    else:
        edad_cuat = input("Ingrese el cuatrimestre de la nueva materia (1-2): ")

        while edad_cuat.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad_cuat = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")
        edad_cuat = int(edad_cuat)

        while edad_cuat < 1 or edad_cuat > 2:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            edad_cuat = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")

            while edad_cuat.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                edad_cuat = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")
            edad_cuat = int(edad_cuat)


    #Pedir año de cursada / carga horaria
    if titulo == "ESTUDIANTES":
        anio = input("Ingrese el año de cursada del nuevo estudiante (1-9): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")
        anio = int(anio)

        while anio < 1 or anio > 9:
            print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
            anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")

            while anio.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")
            anio = int(anio)
    else:
        anio = input("Ingrese el año de la nueva materia (1-5): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")
        anio = int(anio)

        while anio < 1 or anio > 5:
            print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
            anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")

            while anio.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")
            anio = int(anio)


    #Nombre de usuario / año 
    if titulo == "ESTUDIANTES":
        usuario_horaria = nombre.split()
        cont = 1
        numero = 0
        for i in range(len(matriz)):
            if re.search(nombre, matriz[i][1], re.IGNORECASE):
                if cont < len(usuario_horaria[0]):
                    cont += 1
                else: 
                    numero += 1
        if numero == 0:
            usuario_horaria = (usuario_horaria[0][:cont] + usuario_horaria[1]).lower()
        else:
            usuario_horaria = (usuario_horaria[0][:cont] + usuario_horaria[1] + str(numero)).lower()
        print(usuario_horaria)

    else:
        usuario_horaria = input("Ingrese la carga horaria de la nueva materia (1-12): ")

        while usuario_horaria.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            usuario_horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")
        usuario_horaria = int(usuario_horaria)

        while usuario_horaria < 1 or usuario_horaria > 12:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            usuario_horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")

            while usuario_horaria.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                usuario_horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")
            usuario_horaria = int(usuario_horaria)


        
    codigo = matriz[len(matriz) - 1][0] + 1

    #Agregar
    matriz.append([codigo, nombre, edad_cuat, anio, usuario_horaria])

    if titulo == "ESTUDIANTES":
        print(f"{VERDE}Estudiante {codigo} agreagado.{RESET}")
        
    else: 
        print(f"{VERDE}Materia {codigo} agreagada.{RESET}")
    

#------------------ BAJAS ESTUDIANTES / MATERIAS ---------------------
def bajas_estudiantes_materias(matriz, notas, titulo):
    print()
    print(f" == BAJAS {titulo} ==")

    if titulo == "ESTUDIANTES":
        codigo = input("Ingrese el código del estudiante a eliminar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código del estudiante a eliminar (Formato: 100): ")

        codigo = int(codigo)
        esta_en_calificaciones = busqueda_secuencial(notas, 2, codigo)

    else:
        codigo = input("Ingrese el código de la materia a eliminar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la materia a eliminar (Formato: 100): ")

        codigo = int(codigo)
        esta_en_calificaciones = busqueda_secuencial(notas, 3, codigo)

    registrado = busqueda_secuencial(matriz, 0, codigo)

    while registrado == -1 or esta_en_calificaciones != -1:
        if registrado == -1:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        else:
            if titulo == "ESTUDIANTES":
                print(f"{ROJO}ERROR: Ese estudiante tiene una calificaión registrada, no se puede eliminar{RESET}")
            else:
                print(f"{ROJO}ERROR: Esa materia tiene una calificaión registrada, no se puede eliminar{RESET}")

        if titulo == "ESTUDIANTES":
            codigo = input("Ingrese el código del estudiante a eliminar (Formato: 100): ")

            while codigo.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
                codigo = input("Ingrese de nuevo el código del estudiante a eliminar (Formato: 100): ")

            codigo = int(codigo)
            esta_en_calificaciones = busqueda_secuencial(notas, 2, codigo)

        else:
            codigo = input("Ingrese el código de la materia a eliminar (Formato: 100): ")

            while codigo.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
                codigo = input("Ingrese de nuevo el código de la materia a eliminar (Formato: 100): ")

            codigo = int(codigo)
            esta_en_calificaciones = busqueda_secuencial(notas, 3, codigo)

        registrado = busqueda_secuencial(matriz, 0, codigo)

                    

    matriz.pop(registrado)
    
    if titulo == "ESTUDIANTES":
        print(f"{NARANJA}Estudiante {codigo} eliminado.{RESET}")
    else: 
        print(f"{NARANJA}Materia {codigo} agreagada.{RESET}")
    

#------------------ MODIFICACION ESTUDIANTES / MATERIAS ---------------------
def modificar_estudiantes_materias(matriz, titulo):
    print()
    print(f" == MODIFICACIÓN {titulo} ==")
    
    #Pedir el codigo a modificar
    if titulo == "ESTUDIANTES":
        codigo = input("Ingrese el código del estudiante a modificar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código del estudiante a modificar (Formato: 100): ")

        codigo = int(codigo)

    else:
        codigo = input("Ingrese el código de la materia a modificar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

        codigo = int(codigo)

    modificar = busqueda_secuencial(matriz, 0, codigo)

    while modificar == -1:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")

        if titulo == "ESTUDIANTES":
            codigo = input("Ingrese de nuevo el código del estudiante a modificar (Formato: 100): ")

            while codigo.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
                codigo = input("Ingrese de nuevo el código del estudiante a modificar (Formato: 100): ")

            codigo = int(codigo)

        else:
            codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

            while codigo.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
                codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

            codigo = int(codigo)

        modificar = busqueda_secuencial(matriz, 0, codigo)
                
                
#Pedir nombre del estudiante/materia
    if titulo == "ESTUDIANTES":
        nombre = input("Ingrese el nombre y apellido del estudiante: ").title()

        if len(nombre.split()) != 2:
            print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
            nombre = input("Ingrese otra vez el nombre y apellido del estudiante: ").title()

        nombre = nombre.split()
        nombre = nombre[0] + " " + nombre[1]
    else:
        nombre = input("Ingrese el nombre de la materia: ").title()
    
    
#Pedir edad/cuatrimestre
    if titulo == "ESTUDIANTES":
        edad_cuat = input("Ingrese la edad del estudiante: ")

        while edad_cuat.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad_cuat = input("Ingrese de nuevo la edad del estudiante: ")
        edad_cuat = int(edad_cuat)
        
        while edad_cuat < 17 or edad_cuat > 100:
            print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
            edad_cuat = input("Ingrese de nuevo la edad del estudiante: ")

            while edad_cuat.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                edad_cuat = input("Ingrese de nuevo la edad del estudiante: ")
            edad_cuat = int(edad_cuat)
    else:
        edad_cuat = input("Ingrese el cuatrimestre de la materia (1-2): ")

        while edad_cuat.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad_cuat = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")
        edad_cuat = int(edad_cuat)

        while edad_cuat < 1 or edad_cuat > 2:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            edad_cuat = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")

            while edad_cuat.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                edad_cuat = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")
            edad_cuat = int(edad_cuat)


    #Pedir año de cursada / carga horaria
    if titulo == "ESTUDIANTES":
        anio = input("Ingrese el año de cursada del estudiante (1-9): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")
        anio = int(anio)

        while anio < 1 or anio > 9:
            print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
            anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")

            while anio.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")
            anio = int(anio)
    else:
        anio = input("Ingrese el año de la materia (1-5): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese de nuevo el año de la materia (1-5): ")
        anio = int(anio)

        while anio < 1 or anio > 5:
            print(f"{ROJO}Año invalido: rango perimitido de 1 a 5 años{RESET}")
            anio = input("Ingrese de nuevo el año de la materia (1-5): ")

            while anio.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                anio = input("Ingrese de nuevo el año de la materia (1-5): ")
            anio = int(anio)


     #Nombre de usuario / año 
    if titulo == "ESTUDIANTES":
        usuario_horaria = nombre.split()
        cont = 1
        numero = 0
        for i in range(len(matriz)):
            if re.search(nombre, matriz[i][1], re.IGNORECASE):
                if cont < len(usuario_horaria[0]):
                    cont += 1
                else: 
                    numero += 1
        if numero == 0:
            usuario_horaria = (usuario_horaria[0][:cont] + usuario_horaria[1]).lower()
        else:
            usuario_horaria = (usuario_horaria[0][:cont] + usuario_horaria[1] + str(numero)).lower()
        print(usuario_horaria)

    else:
        usuario_horaria = input("Ingrese la carga horaria de la materia (1-12): ")

        while usuario_horaria.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            usuario_horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")
        usuario_horaria = int(usuario_horaria)

        while usuario_horaria < 1 or usuario_horaria > 12:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            usuario_horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")

            while usuario_horaria.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
                usuario_horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")
            usuario_horaria = int(usuario_horaria)

        

    #Modificar
    matriz[modificar][0] = codigo
    matriz[modificar][1] = nombre
    matriz[modificar][2] = edad_cuat
    matriz[modificar][3] = anio
    matriz[modificar][4] = usuario_horaria

    if titulo == "ESTUDIANTES":
        print(f"{AZUL}Estudiante {codigo} modificado.{RESET}")
    else: 
        print(f"{AZUL}Materia {codigo} modificada.{RESET}")
        
        

#------------------ MOSTRAR ESTUDIANTES / MATERIAS ---------------------   
def imprimir_matriz(matriz, titulo):

    if titulo == "ESTUDIANTES":
        print("="*82)
        print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
        print("="*82)
        print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{"Usuario":>19}{RESET}")
        print("-" * 82)
    else:
        print("="*82)
        print(f'{BOLD}{MAGENTA}{"MATERIAS":^82}{RESET}')
        print("="*82)
        print(f"{BOLD}{'Id Materia':<16}{'Nombre':<21}{'Cuatrimestre':^12}{"Año":^17}{'Carga Horaria':^13}{RESET}")
        print("-" * 82)

        lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), matriz))
        for fila in range(len(matriz)):
            matriz[fila][0] = lista_codigo[fila]

    # Datos
    for i in range(len(matriz)):
        codigo = matriz[i][0]

        nombre = matriz[i][1]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        edad_cuat = matriz[i][2]
        anio = matriz[i][3]

        usuario_horaria = matriz[i][4]

        if titulo == "ESTUDIANTES":
            if len(usuario_horaria) > 15:
                usuario_horaria = usuario_horaria[:12] + "..."
            print(f"{codigo:<13}{nombre:<17}{edad_cuat:^18}{anio:^13}{usuario_horaria:>19}")
        else:
            print(f"{codigo:<16}{nombre:<21}{edad_cuat:^12}{anio:^17}{usuario_horaria:^13}")



def ordenar_matriz(matriz, columna, reversa):
    if reversa == 0: 
        matriz.sort(key=lambda fila: fila[columna])
    else:
        matriz.sort(key=lambda fila: fila[columna], reverse=True)



def mostrar_estudiantes_materias(matriz, titulo):
    columna = input("Ingrese el número de la columna para ordenar (1-4): ")

    while columna.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 4{RESET}")
        columna = input("Ingrese el número de la columna para ordenar (1-4): ")
    columna = int(columna) - 1

    while columna < 0 or columna > 3:
        print(f"{ROJO}Número inválido, la matriz posee 4 columnas{RESET}")
        columna = input("Ingrese de nuevo el número de la columna para ordenar (1-4): ")

        while columna.isnumeric() == False:
            print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 4{RESET}")
            columna = input("Ingrese el número de la columna para ordenar (1-4): ")
        columna = int(columna) - 1

    
    reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")

    while reversa.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 2{RESET}")
        reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")
    reversa = int(reversa)
    
    while reversa < 0 or reversa > 1:
        print(f"{ROJO}Número inválido, rango valido de 0 a 1{RESET}")
        reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")

        while reversa.isnumeric() == False:
            print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 2{RESET}")
            reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")
        reversa = int(reversa)

    ordenar_matriz(matriz, columna, reversa)
    imprimir_matriz(matriz, titulo)



# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"