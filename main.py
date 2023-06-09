import json
import os
from paquete import Cliente
from paquete.Cliente import Cliente
from paquete.Cliente import Guardar
from paquete.Cliente import basedatos
from paquete import Televisores
from paquete.Televisores import Televisores

cliente = None
while True:
    print(" B i E n V e N i d @  a  TV MUNDO. \n Registrese, inicie sesion, LLene el carrito y acceda al pago") 
    print("1.- R e G i S t R a R s E")
    print("2.- I n I c I e  S e S i O n")
    print("3.- L l e n e  e l  c a r r i t o")
    print("4.- S a l i r")

    opcion = input("Seleccione una opcion (del 1 al 4):")

    if (opcion == "1"):
        nombreCompleto = input("Ingrese su nombre completo: ")
        usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        email = input("Ingrese un correo electrónico: ")
        direccion_envio = input("Ingrese su dirección: ")
        os.system("cls")
        cliente = Cliente(nombreCompleto, usuario, contraseña, email, direccion_envio)
        cliente.registrarse(basedatos)
        Guardar(basedatos)
    
    elif (opcion == '2'):
        usuario = input("Nombre de Usuario: ")
        contraseña = input("Contraseña: ")
        os.system("cls")
        cliente = Cliente("", usuario, contraseña, "", "")
        cliente.iniciar_sesion(basedatos)
        input("Enter, si desea continuar . . ")
    
    elif (opcion == '3'):
        if cliente is None:
            print("Iniciar Sesion antes de llenar el carrito.")
            input("Enter para continuar . . .")
        else:
            televisores = Televisores("", "", "", 0)
            televisores.comprar(cliente, basedatos)
    
    elif opcion == "4":
        print("Muchas gracias por la visita, de parte de TV MUNDO. Recuerde que la pagina se actualiza dia a dia ")
        break

    else:
        print("O p C i O n  I n C o r r E c T a (Seleccione una opcion correcta, por favor)")
        input("Enter para continuar. . .")   
        
Guardar (basedatos)







