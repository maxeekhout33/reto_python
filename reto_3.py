users = []
new_users = int (input('Porfavor indica cuantos usuarios deseas registrar: '))

for i in range(1, new_users + 1): # Argumentos: inicio en id = 1 y termino en la cantidad ingresada +1

    name = input("Ingrese su nombre: ")
    while len(name) < 5 or len(name) > 50:
        print("El nombre debe tener una longitud mínima de 5 caracteres y máxima de 50.")
        name = input("Ingrese su nombre: ")
    # print("Nombre válido: ", name)

    last_name = input("Ingrese su apellido: ")
    while len(last_name) < 5 or len(last_name) > 50:
        print("El apellido debe tener una longitud mínima de 5 caracteres y máxima de 50.")
        last_name = input("Ingrese su apellido: ")
    # print("Apellido válido: ", last_name)

    phone_number = input ("Ingrese su número de teléfono: ")
    while len(phone_number) != 10:
        print("El número debe tener una longitud de 10 digitos exactos")
        phone_number = input("Ingrese su número de teléfono: ")
    # print("Número de teléfono válido: ", phone_number)

    email = input ("Ingrese su correo electrónico: ")
    while len(email) < 5 or len(email) > 50:
        print("El correo electrónico debe tener una longitud mínima de 5 caracteres y máxima de 50.")
        email = input("Ingrese su correo electrónico: ")
    # print("Correo electrónico válido: ", email)

    print('>>> Hola ' + name + ' ' + last_name + ', en breve recibirás un correo a ' + email)
    user = (i, name, last_name, phone_number, email)
    users.append(user)

print('Usuarios registrados:')
for user in users:
    print(user)