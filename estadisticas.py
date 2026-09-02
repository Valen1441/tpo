def estadisticas_materias(notas, materias):

    for materia in materias:
        id_materia = materia[0]
        nombre = materia[1]

        suma = 0
        cantidad = 0
        cant_ap = 0
        cant_pro = 0
        cant_des = 0

        for nota in notas:
            if nota[3] == id_materia:
                suma += nota[1]
                cantidad += 1
                if nota[4] == 1:
                    cant_ap += 1
                if nota[4] == 2:
                    cant_pro += 1
                else:
                    cant_des += 1

        if cantidad > 0:
            promedio = (lambda a,b: a / b)(suma, cantidad)

           
        else:
            ...