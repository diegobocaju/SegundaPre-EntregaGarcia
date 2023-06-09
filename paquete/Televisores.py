from paquete import Cliente
from paquete.Cliente import Cliente

class Televisores:
    def __init__(self,marca,tipo, pulgadas,precio):
        self.marca = marca
        self.tipo = tipo
        self.pulgadas = pulgadas
        self.precio = float(precio)
    
    def __str__(self):
        mostrar = f'{self.marca} -- {self.tipo} -- {self.pulgadas} -- ${self.precio}'
        return mostrar
    
    def comprar(self,cliente,basededatos):
        if not cliente.iniciar_sesion(basededatos):
            return
        
        televisores_en_stock = [
            Televisores('Samsung','Smart TV Ultra HD 4K', '65 pulgadas', '256799'),
            Televisores('Philips','Smart TV LED','43 Pulgadas', '118999'),
            Televisores('TCL','Smart TV Ultra HD 4K','65 Pulgadas','249999'),
            Televisores('Hisense','Smart TV Ultra HD 4K','75 Pulgadas','471199'),
            Televisores('Hitachi','Smart TV Ultra HD 4K','50 Pulgadas','148999'),
            Televisores('BGH','Smart TV Ultra HD','43 pulgadas', '91199')
        ]

        televisores_seleccionados = []

#Televisores disponibles
        print("Televisores disponibles: ")      
        for indice, televisor in enumerate(televisores_en_stock):
            print (f"{indice+1} - {televisor}")   
        while True:
            opcion = input("Indique que televisor quiere (indique con un numero de 1 a 6) : ")
            print("Con el 0 finalizas ")
            if opcion == "0":
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(televisores_en_stock):
                televisor_seleccionado = televisores_en_stock[int(opcion) - 1]
                televisores_seleccionados.append(televisor_seleccionado)
                print(f"El televisor {televisor_seleccionado.marca} - {televisor_seleccionado.tipo} de {self.pulgadas} ha sido sumado a su carrito")
            else:
                print("Opcion  E R R O N E A!. Indique un número válido.")       

        if televisores_seleccionados:
            print("\nResumen de compra:")
            total = 0
            for televisor in televisores_seleccionados:
                print(f"{televisor.marca} - {televisor.tipo} de {televisor_seleccionado.pulgadas} - ${televisor.precio}")
                total += televisor.precio
            print(f"\nTotal: ${total}")
            print("Orden de Compra:")
            print(f"Cliente: {cliente.nombre_completo}")
            print(f"Email: {cliente.email}")
            print(f"Dirección: {cliente.direccion_envio}")
            print("La orden de compra se enviará a su email para ser abonada")
        else:
            print("No se agregaron televisores a su carrito. La compra se canceló.")
        
        input("Si desea continuar presione el  E N T E R")




    
    
    

