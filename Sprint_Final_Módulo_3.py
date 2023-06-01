import random
import string

# crea nombre de usuario a partir del nombre #
def cuentas(nombre):
    nombreusuario = "Usuario_" + nombre.lower()
    
    # crear contraseña con numeros/letras aleatorios (le puse un máximo de 8 caracteres a la contraseña para que no sea tan larga ni tan corta) #
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(8))
    
    return nombreusuario, contrasena

# nombres de los 10 nuevos usuarios #
nombres_usuarios = [
    {'nombre':'nombre1'},
    {'nombre':'nombre2'},
    {'nombre':'nombre3'},
    {'nombre':'nombre4'},
    {'nombre':'nombre5'},
    {'nombre':'nombre6'},
    {'nombre':'nombre7'},
    {'nombre':'nombre8'},
    {'nombre':'nombre9'},
    {'nombre':'nombre10'},
]

# contenedor de usuarios creados y sus contraseñas #
usuarios = []

# crear las cuentas para cada usuario de la lista nombres_usuarios #
for nombre_usuario in nombres_usuarios:
    nombre = nombre_usuario['nombre']
    username, password = cuentas(nombre)
    usuario = {'nombre': nombre, 'Nombre de usuario': username, 'contraseña': password}
    usuarios.append(usuario)


# pedir numero telefónico y seguir pidiendolo hasta que cada usuario lo haya registrado ¡se actualiza longitud de telefono acorde a requerimiento del trabajo! #
for usuario in usuarios:
    while True:
        telefono = input(f"Ingresa el número telefónico para {usuario['nombre']}: ")
        if telefono.isdigit() and len(telefono) >= 8:
            usuario['telefono'] = telefono
            break
        else:
            print("Ingresa un teléfono válido de 8 dígitos")


# Imprime las cuentas de los usuarios #
for usuario in usuarios:
    print("Nombre:", usuario['nombre'])
    print("Nombre de usuario:", usuario['Nombre de usuario'])
    print("Contraseña:", usuario['contraseña'])
    print("Teléfono:","#" + usuario['telefono'])
    print()