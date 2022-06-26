import numpy as np
#arange =Rellena la lista con un rango inicio,fin
#reshape = organiza el arreglo nuevamente por filas y columna
asientos=np.arange(1,43).reshape((7,6))
clientes=np.array(())

while True:
    try:
        print("Bienvenido/a, para continuar debe ingresar con sus datos que le seran pedidos, favor de seguir las instrucciones:\n")
        
        registrar = input("desea registrar cliente?, (si - no)\n").lower().strip()
        
        if registrar == "si" :
        
            nombre = input("Ingrese su nombre:\n")
            rut = int(input("Ingrese su rut, sin guion, si digito verificador:\n"))
            fono = int(input("Ingrese su número de contacto:\n"))
            banco = input("Es usuario de BancoDuoc?, (si - no):\n").lower().strip()
            if banco == "si":
                print("Tendra un Dcto del '15%' en su reservacion, gracias.")
        else :
        
            print("\nMenu: ")
            print("1.- Ver asientos disponibles \n2.- Comprar asiento \n3.- Anular vuelo \n4.- Modificar datos de pasajero \n5.- Salir")

            opt=int(input("Seleccione la opcion que desea: "))

            if opt == 1:

                print(f"los asientos disponibles son: \n{asientos}")
            
            elif opt == 2:
                
                print("El valor de los asientos son los siguintes\n")
                print("1.- Normal: $78.900 \n2.- Premium: $240.000")
                
            elif opt == 3:
                
                print("Si desea anular el vuelo debe ingresar los datos del cliente: ")
            
            elif opt == 5:
                
                break
            
            else:
                
                print("Opción ingresada incorrecta")
                
            seguir = input("Desea volver al menú?: (si - no)\n").lower().strip()
            
            if seguir != "si":
                
                break

        


    
    except ValueError:
        print("El valor debe ser entre 1 a 4 ")