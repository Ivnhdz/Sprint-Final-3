'''
programa que recorra una liste que se le agreguen maximo 10 usuarios de lo que sea  -------------------------------OK

funcion para crearle una cuenta automaticamente -------------------------------------------------------------------OK

asignar una contraseña a cada cuenta, debe crearse con random y debe tener mayuscula, minuscula y numeros ---------OK

cada cuenta debe guardarse en una nueva variable con su contraseña ------------------------------------------------OK

Por cada cuenta debe pedir un número telefónico para contactarse. -------------------------------------------------OK

el programa no terminará de preguntar por los numeros hasta que todas las cuentas tengan un numero de contacto asignado OK

el programa debe verificar que el numero de telefono tenga 8 digitos numericos (se debe guardar como string) --- OK

entregar en un word o pdf con la ruta del repositorio github

'''
import random
import string

# crea nombre de usuario a partir del nombre #
def cuentas(nombre):
    nombreusuario = "Usuario_" + nombre.lower()
    
    # crear contraseña con numeros/letras aleatorios #
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(8))
    
    return nombreusuario, contrasena

# contenedor de los 10 nuevos usuarios #
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
    usuario = {'nombre': nombre, 'username': username, 'password': password}
    usuarios.append(usuario)


# pedir numero telefónico y seguir pidiendolo hasta que cada usuario lo haya registrado #
for usuario in usuarios:
    while True:
        telefono = input(f"Ingresa el número telefónico para {usuario['nombre']}: ")
        if telefono.isdigit() and len(telefono) >= 8:
            usuario['telefono'] = telefono
            break
        else:
            print("Ingresa un teléfono válido de 8 dígitos")


# Imprimir las cuentas de los usuarios #
for usuario in usuarios:
    print("Nombre:", usuario['nombre'])
    print("Nombre de usuario:", usuario['username'])
    print("Contraseña:", usuario['password'])
    print("Teléfono: #", usuario['telefono'])
    print()