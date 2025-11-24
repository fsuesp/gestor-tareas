from gestor import Gestor_tareas


gestor = Gestor_tareas()


while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Ordenar por prioridad")
    print("0. Salir")


    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        gestor.agregar_tarea()
    elif opcion == "2":
        gestor.listar_tareas()
    elif opcion == "3":
        gestor.completar_tarea()
    elif opcion == "4":
        gestor.eliminar_tarea()
    elif opcion == "5":
        gestor.ordenar_por_prioridad()
    elif opcion == "0":
        gestor.guardar_tareas()
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")