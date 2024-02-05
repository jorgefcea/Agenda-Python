from bson import ObjectId

class Agenda:
    def __init__(self, cliente, nombre_bd, nombre_coleccion):
        self.cliente = cliente
        self.db = self.cliente[nombre_bd]
        self.coleccion = self.db[nombre_coleccion]
        self.contactos = []

    def insertar_contacto(self, Nombre, Apellidos, Telefono, Email):
        contacto = {"Nombre": Nombre, "Apellidos": Apellidos, "Telefono": Telefono, "Email": Email}
        self.coleccion.insert_one(contacto)
        self.contactos.append(contacto)
        print()
        print("El contacto ha sido creado.")

    def borrar_contacto(self, id):
        resultado = self.coleccion.delete_one({"_id": ObjectId(id)})
        
        if resultado.deleted_count == 0:
            print()
            print("No se encontró ningún contacto con el ID especificado.")
        else:
            print()
            print("El contacto ha sido eliminado.")

    def buscar_contacto(self, Nombre, Apellidos):
        resultados = self.coleccion.find({"Nombre": Nombre, "Apellidos": Apellidos})

        lista_resultados = list(resultados)

        if len(lista_resultados) == 0:
            print()
            print("No se encontró ningún contacto con el Nombre y Apellidos especificados.")
        else:
            print()
            print("El resultado de la búsqueda es:")
            print()
            for resultado in lista_resultados:
                print("Nombre:", resultado["Nombre"])
                print("Apellidos:", resultado["Apellidos"])
                print("Teléfono:", resultado["Telefono"])
                print("Email:", resultado["Email"])

    def actualizar_contacto(self, id, Nombre=None, Apellidos=None, Telefono=None, Email=None):
        campos_actualizados = {}
        if Nombre:
            campos_actualizados["Nombre"] = Nombre
        if Apellidos:
            campos_actualizados["Apellidos"] = Apellidos
        if Telefono:
            campos_actualizados["Telefono"] = Telefono
        if Email:
            campos_actualizados["Email"] = Email

        resultado = self.coleccion.update_one({"_id": ObjectId(id)}, {"$set": campos_actualizados})

        if resultado.modified_count == 0:
            print()
            print("No se encontró ningún contacto con el ID especificado.")
        else:
            print()
            print("El contacto ha sido actualizado.")
            
    def ver_todos_contactos(self):
        resultados = self.coleccion.find({})
        contactos = []
        print()
        print("Listado de contactos:")
        print()
        for resultado in resultados:
            print("Nombre:", resultado["Nombre"])
            print("Apellidos:", resultado["Apellidos"])
            print("Teléfono:", resultado["Telefono"])
            print("Email:", resultado["Email"])
            print()
            contactos.append(resultado)
        return contactos
        

    def sacar_id(self, Nombre, Apellidos):
        resultado = self.coleccion.find_one({"Nombre": Nombre, "Apellidos":Apellidos})
        id_contacto = str(resultado["_id"])
        return id_contacto
    
    def contacto_existe (self, Nombre, Apellidos):
        resultados = self.coleccion.find({"Nombre": Nombre, "Apellidos":Apellidos})
        if resultados:
            return True
        else:
            return False