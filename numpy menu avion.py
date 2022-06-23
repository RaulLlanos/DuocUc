import numpy as np

#arange =Rellena la lista con un rango inicio,fin
#reshape = organiza el arreglo nuevamente por filas y columna

asientos=np.arange(1,43).reshape((7,6))
print (asientos)

opt = 0

while opt != 5:
    
    try :
        
        print("Menu: ")
        print("1.- Ver asientos disponibles \n2.- Comprar asiento \n3.- Anular vuelo \n4.- Modificar datos de pasajero \n5.- Salir")
        
        opt=int(input("Seleccione la opcion que desea: "))
        
        if opt == 1 :
            
            print(f"los asientos disponibles son: \n{asientos}")
            
        if opt == 2:
            
            print("El valor de los asientos son los siguintes\n")
            print("1.- Normal: $78.900 \n2.- Premium: $240.000")
        
        
    
    except ValueError:
        print("El valor debe ser entre 1 a 4 ")
    if opt > 4:
        raise Exception("Opcion debe estar entre 1 a 4")
