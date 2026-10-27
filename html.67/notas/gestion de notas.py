estudiantes = [] 
while True:
    print("\n--- MENÚ ---")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Calcular promedio de un estudiante")
    print("4. Mostrar estudiantes aprobados")
    print("5. Mostrar estudiante con mayor promedio")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        notas = []
        cantidad = int(input("¿Cuántas notas tiene? "))
        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        estudiante = {"nombre": nombre, "notas": notas}
        estudiantes.append(estudiante)
        print("Estudiante registrado correctamente.")

    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nEstudiantes registrados:")
            for e in estudiantes:
                print("-", e["nombre"], "| Notas:", e["notas"])

    elif opcion == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            nombre = input("Nombre del estudiante: ")
            encontrado = False
            for e in estudiantes:
                if e["nombre"].lower() == nombre.lower():
                    suma = 0
                    for n in e["notas"]:
                        suma = suma + n
                    promedio = suma / len(e["notas"])
                    print(f"El promedio de {e['nombre']} es: {promedio:.2f}")
                    encontrado = True
            if encontrado == False:
                print("Estudiante no encontrado.")

    elif opcion == "4":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nEstudiantes aprobados (promedio >= 3.0):")
            hay_aprobados = False
            for e in estudiantes:
                suma = 0
                for n in e["notas"]:
                    suma = suma + n
                promedio = suma / len(e["notas"])
                if promedio >= 4.0:
                    print(f"- {e['nombre']} con promedio {promedio:.2f}")
                    hay_aprobados = True
            if hay_aprobados == False:
                print("Ningún estudiante está aprobado.")

    elif opcion == "5":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            mejor = estudiantes[0]
            suma = 0
            for n in mejor["notas"]:
                suma = suma + n
            mejor_promedio = suma / len(mejor["notas"])

            for e in estudiantes:
                suma = 0
                for n in e["notas"]:
                    suma = suma + n
                promedio = suma / len(e["notas"])
                if promedio > mejor_promedio:
                    mejor_promedio = promedio
                    mejor = e

            print(f"El estudiante con mayor promedio es: {mejor['nombre']} con {mejor_promedio:.2f}")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
