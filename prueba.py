users = {}

while True:
    print("\n--- Menú ---")
    print("1. Agregar nuevo usuario")
    print("2. Listar IDs de usuarios registrados")
    print("3. Ver información de un usuario por ID")
    print("4. Editar información de un usuario por ID")
    print("5. Salir")

    choice = input("Seleccione una opción (1-5): ")

    if choice == "1":
        user_id = len(users) + 1
        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        phone_number = input("Ingrese su número de teléfono: ")
        email = input("Ingrese su correo electrónico: ")

        users[user_id] = {
            "name": name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email
        }

        print(f"Usuario {user_id} registrado correctamente.")
    elif choice == "2":
        print("\nIDs de usuarios registrados:")
        for user_id in users:
            print(user_id)
    elif choice == "3":
        user_id = int(input("Ingrese el ID del usuario que desea consultar: "))
        if user_id in users:
            user = users[user_id]
            print(f"\nInformación del usuario {user_id}:")
            print(f"Nombre: {user['name']}")
            print(f"Apellido: {user['last_name']}")
            print(f"Número de teléfono: {user['phone_number']}")
            print(f"Correo electrónico: {user['email']}")
        else:
            print(f"No se encontró ningún usuario con el ID {user_id}.")
    elif choice == "4":
        user_id = int(input("Ingrese el ID del usuario que desea editar: "))
        if user_id in users:
            user = users[user_id]
            print(f"\nEditando información del usuario {user_id}:")
            user["name"] = input("Nuevo nombre: ")
            user["last_name"] = input("Nuevo apellido: ")
            user["phone_number"] = input("Nuevo número de teléfono: ")
            user["email"] = input("Nuevo correo electrónico: ")
            print(f"Información del usuario {user_id} actualizada correctamente.")
        else:
            print(f"No se encontró ningún usuario con el ID {user_id}.")
    elif choice == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")