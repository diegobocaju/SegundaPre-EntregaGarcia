import json
class Cliente:
    def __init__(self,nombre_completo,usuario, contraseña, email, direccion_envio):
        self.nombre_completo = nombre_completo
        self.usuario = usuario
        self.contraseña = contraseña
        self.email = email
        self. direccion_envio = direccion_envio
    
    def __str__(self):
        mostrar = print(f'Cliente: {self.nombre_completo}/n Email: {self.email} /n  Direccion: {self.direccion_envio}')
        return mostrar
    
    def registrarse (self, basedatos):
        if self.usuario is not basedatos:
            basedatos[self.usuario] ={
                'Nombre Completo' : self.nombre_completo,
                'Usuario': self.usuario,
                'Contraseña': self.contraseña,
                'Email': self.email,
                'Direccion de envío': self.direccion_envio
            }
            print(f"¡El usuario {self.usuario} se registró")
            return self.nombre_completo, self.email, self.direccion_envio
        else:
            print(f"El usuario {self.usuario} ya existe en la base de datos.")
            return None,None,None
    
    def iniciar_sesion(self,basedatos):
            if self.usuario in basedatos and basedatos[self.usuario]['Contraseña'] == self.contraseña:
                datosusuario = basedatos[self.usuario]
                self.nombre_completo = datosusuario['Nombre Completo']
                self.email = datosusuario['Email']
                self.direccion_envio = datosusuario['Direccion de envío']
                print(f"BiEnVeNiDo {self.nombre_completo}")
                return True
            else:
                print("Usuario y/o contraseña E R R O N E A")
                return False
            
def Cargar():
    try:
        with open("./basededatos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def Guardar(basedatos):
    with open("./basededatos.json", "w") as archivo:
        json.dump(basedatos, archivo)

basedatos = Cargar()












    
    






    

