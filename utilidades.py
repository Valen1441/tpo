def busqueda_secuencial(matriz, columna, dato):
    '''
    pre: recibe una matriz, el número de columna donde buscar y el dato a buscar.
    pos: devuelve la posición de la fila donde se encuentra el dato o -1 si no lo encuentra.
    '''
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

def obtener_lista_legajos(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: devuelve una lista que contiene los legajos de todos los estudiantes.
    '''
    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos