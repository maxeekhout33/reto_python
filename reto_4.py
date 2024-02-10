users = {}

while True:
    print("\n --- Menu ---")
    print("1. Agregar nuevo(s) usuario(s)")
    print("2. Listar IDs de usuarios registrados")
    print("3. Ver información de un usuario por ID")
    print("4. Editar información de un usuario por ID")
    print("5. Salir")

    option = input("Ingrese una opcion: ")

    if option == '1':
        amount = int(input("Porfavor indica cuantos usuarios deseas registrar: "))
        for i in range(amount): 
            user_id = len(users) + 1

            name = input("Ingrese su nombre: ")
            while len(name) < 5 or len(name) > 50:
                print(
                    "El nombre debe tener una longitud mínima de 5 caracteres y máxima de 50."
                )
                name = input("Ingrese su nombre: ")

            last_name = input("Ingrese su apellido: ")
            while len(last_name) < 5 or len(last_name) > 50:
                print(
                    "El apellido debe tener una longitud mínima de 5 caracteres y máxima de 50."
                )
                last_name = input("Ingrese su apellido: ")

            phone_number = input("Ingrese su número de teléfono: ")
            while len(phone_number) != 1:
                print("El número debe tener una longitud de 10 digitos exactos")
                phone_number = input("Ingrese su número de teléfono: ")

            email = input("Ingrese su correo electrónico: ")
            while len(email) < 5 or len(email) > 50:
                print(
                    "El correo electrónico debe tener una longitud mínima de 5 caracteres y máxima de 50."
                )
                email = input("Ingrese su correo electrónico: ")

            print(
                '>>> Hola '+ name + ' ' + last_name + ', en breve recibirás un correo a ' + email
            )
            users[user_id] = {
                'ID': user_id,
                'name': name,
                'last_name': last_name,
                'phone_number': phone_number,
                'email': email,
            }

    elif option == '2':
        print('\nIDs de usuarios registrados:')
        for user_id in users:
            user = users[user_id]
            print(user.get('ID'))

    elif option == '3':
        user_id = int(input('Ingrese el ID del usuario que desea consultar: '))
        if user_id in users:
            user = users[user_id]
            print(f'\nInformación del usuario {user_id}:')
            print(f'Nombre: {user["name"]}')
            print(f'Apellido: {user["last_name"]}')
            print(f'Número de teléfono: {user["phone_number"]}')
            print(f'Correo electrónico: {user["email"]}')
        else:
            print(f'No se encontró ningún usuario con el ID {user_id}.')

    elif option == '4':
            user_id = int(input('Ingrese el ID del usuario que desea editar: '))
            if user_id in users:
                user = users[user_id]
                print(f'\nEditando información del usuario {user_id}:')
                user['name'] = input('Nuevo nombre: ')
                user['last_name'] = input('Nuevo apellido: ')
                user['phone_number'] = input('Nuevo número de teléfono: ')
                user['email'] = input('Nuevo correo electrónico: ')
                print(f'Información del usuario {user_id} actualizada correctamente.')
            else:
                print(f'No se encontró ningún usuario con el ID {user_id}.')

    elif option == '5':
            print('¡Hasta luego!')
            break
    
    else:
        print('Opción inválida. Intente nuevamente.')