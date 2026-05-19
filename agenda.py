
agenda = [
    {"nombre": "Carlos Alcaraz", "telefono": "611223344"},
    {"nombre": "Sofia DAW", "telefono": "655998877"}
]

def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Ver contactos")
    print("2. Añadir contacto")
    print("3. Buscar contacto por nombre")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = input("Selecciona una opción (1-5): ").strip()
        except EOFError:
            break
        
        if opcion == "1":
            print("\n--- LISTA DE CONTACTOS ---")
            if not agenda:
                print("La agenda está vacía.")
            else:
                for idx, contacto in enumerate(agenda, 1):
                    print(f"{idx}. Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']}")
        elif opcion == "2":
            print("\n--- AÑADIR CONTACTO ---")
            nombre = input("Introduce el nombre completo: ").strip()
            telefono = input("Introduce el número de teléfono: ").strip()
            if nombre and telefono:
                nuevo_contacto = {"nombre": nombre, "telefono": telefono}
                agenda.append(nuevo_contacto)
                print(f"¡Contacto '{nombre}' añadido correctamente!")
            else:
                print("Error: El nombre o el teléfono no pueden estar vacíos.")
        elif opcion == "3":
            print("\n--- BUSCAR CONTACTO ---")
            busqueda = input("Introduce el nombre a buscar: ").strip().lower()
            encontrados = [c for c in agenda if busqueda in c['nombre'].lower()]
            if encontrados:
                print(f"Resultados encontrados ({len(encontrados)}):")
                for c in encontrados:
                    print(f"- Nombre: {c['nombre']} | Teléfono: {c['telefono']}")
            else:
                print("No se encontró ningún contacto con ese nombre.")
        elif opcion == "4":
            print("\n--- ELIMINAR CONTACTO ---")
            nombre_eliminar = input("Introduce el nombre exacto del contacto a borrar: ").strip()
            inicial_len = len(agenda)
            agenda[:] = [c for c in agenda if c['nombre'].lower() != nombre_eliminar.lower()]
            if len(agenda) < inicial_len:
                print(f"¡Contacto '{nombre_eliminar}' eliminado con éxito!")
            else:
                print("No se encontró ningún contacto con ese nombre exacto para eliminar.")
        elif opcion == "5":
            print("\nSaliendo de la agenda de contactos... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona un número entre 1 y 5.")

if __name__ == "__main__":
    main()