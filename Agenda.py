import pymongo, re
from Metodos import Agenda

# Establecer la conexión con la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear la agenda y la colección de contacto
db = client["Agenda"]
coleccion = db["contactos"]
agenda = Agenda(client, "Agenda", "contactos")

# Menu de la agenda
salir = False
numero = 0
while (salir == False):
    print()
    print("AGENDA - MENÚ DE CONTACTOS")
    print("◤-------------------------------◥")
    print("1. Insertar un nuevo contacto")
    print("2. Eliminar un contacto")
    print("3. Buscar contactos por nombre y apellidos")
    print("4. Actualizar un contacto existente")
    print("5. Ver todos los contactos")
    print("6. Salir")
    print("◣-------------------------------◢")
    
    numero = int(input("Elija opción: "))
    
    if numero == 6:
        salir = True
        print("Saliendo de la agenda...")
    elif numero == 1:
        nombre, apellidos, telefono, email = None, None, None, None
        while not all([nombre, apellidos, telefono, email]):
            nombre = input("Ingrese el nombre del contacto: ")
            apellidos = input("Ingrese los apellidos del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            while not re.match(r"^[0-9]{9}$", telefono):
                telefono = input("Ingrese un número de teléfono válido: ")
            email = input("Ingrese el correo electrónico del contacto: ")
            while not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                email = input("Ingrese un correo electrónico válido: ")
            if not all([nombre, apellidos, telefono, email]):
                print("Por favor, asegúrese de ingresar todos los campos.")
        agenda.insertar_contacto(nombre, apellidos, telefono, email)
    elif numero == 2:
        nombre, apellidos = None, None
        while not all([nombre, apellidos]):
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            apellidos = input("Ingrese los apellidos del contacto que desea eliminar: ")
            if not all([nombre, apellidos]):
                print("Por favor, asegúrese de ingresar ambos campos.")
        id = agenda.sacar_id(nombre, apellidos)
        agenda.borrar_contacto(id)
    elif numero == 3:
        nombre, apellidos = None, None
        while not all([nombre, apellidos]):
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            apellidos = input("Ingrese los apellidos del contacto a buscar: ")
            if not all([nombre, apellidos]):
                print("Por favor, asegúrese de ingresar ambos campos.")
        agenda.buscar_contacto(nombre, apellidos)    
    elif numero == 4:
        nombre1, apellidos1 = None, None
        while not all([nombre1, apellidos1]):
            nombre1 = input("Ingrese el nombre del contacto que desea actualizar: ")
            apellidos1 = input("Ingrese los apellidos del contacto que desea actualizar: ")
            if not all([nombre1, apellidos1]):
                print("Por favor, asegúrese de ingresar ambos campos.")
        nombre, apellidos, telefono, email = None, None, None, None
        while not all([nombre, apellidos, telefono, email]):
            nombre = input("Ingrese el nuevo nombre del contacto: ")
            apellidos = input("Ingrese los nuevos apellidos del contacto: ")
            telefono = input("Ingrese el nuevo teléfono del contacto: ")
            while not re.match(r"^[0-9]{9}$", telefono):
                telefono = input("Ingrese un número de teléfono válido: ")
            email = input("Ingrese el nuevo correo electrónico del contacto: ")
            while not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                email = input("Ingrese un correo electrónico válido: ")
            if not all([nombre, apellidos, telefono, email]):
                print("Por favor, asegúrese de ingresar todos los campos.")
        id = agenda.sacar_id(nombre1, apellidos1)
        agenda.actualizar_contacto(id, nombre, apellidos, telefono, email)
    elif numero == 5:
        agenda.ver_todos_contactos()
    else:
        print("Opción inválida, inténtelo de nuevo.")






