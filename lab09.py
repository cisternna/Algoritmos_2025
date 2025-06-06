tareas = []
opcion = ""
while opcion != 5:
    print("1. Agregar tarean\n" 
    "2. Eliminar Tarea\n" 
    "3. Mostrar Tarea\n" 
    "4. Borrar Tareas\n" 
    "5. Salir\n")
    opcion = int(input("Selecciona una opcion:  "))

    if opcion == 1: 
        tareas.append(input("Ingrese el nombre de la tarea: "))
    elif opcion == 2:
        Indice = int(input("Ingrese el Indice de la tarea: "))
        if 0 <= Indice <= len(tareas)-1: tareas.pop(Indice)
        else: 
            print("Indice no valido!\n"
            "Intentar nuevamente")
        print()
    elif opcion == 3:
        for i in tareas:
            print(tareas.index(i),".", i)
        print()
    elif opcion == 4:
        tareas.clear()
        print("Tareas borradas")
    elif opcion == 5: print("Saliendo...")
    else: 
        print("Selecciona una opcion disponible!")
        print()
        continue

