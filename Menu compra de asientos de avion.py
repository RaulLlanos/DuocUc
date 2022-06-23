from site import execsitecustomize
import numpy as np

def operacionAvion(limiteInferior, limiteSuperior, clase, veces):#Ver los asientos, si hay libres o no, escoger el asiento
    
    existeAsientos = False #Si es que no existe asientos es FALSE
    
    print("Los asientos disponibles son: ")
            
    for i in range(limiteInferior, limiteSuperior):
        
        if asientos[i] == False:#Si esta libre el asiento
            
            existeAsientos = True
            
            print(i+1)
    
    if existeAsientos == True:#Si existen asientos
        nroAsiento = int(input("Que asiento desea elegir?: "))
        
        posicion = nroAsiento - 1 #Si escoge el asiento nro 1 quiere decir que escoge la posicion 0
        
        if posicion >= limiteInferior and posicion < limiteSuperior:
            
            if asientos[posicion] == False:#Si ese asiento escogido esta vacio 
                
                asientos[posicion] = True
                
                print(f"El asiento elegido es: {nroAsiento}")
                
            else:
                
                print("Asiento ocupado.")
                
                #No se si usar esta parte ya que reasigna el siguiente asiento y puede que no le guste a la gente
                '''
                for i in range(limiteInferior,limiteSuperior):
                    
                    if asientos[i] == False:#Si esta ocupado
                        
                        print(f"Se le asigna el asiento, {i+1}")
                        
                        asientos[i] = True
                        
                        break
                        '''
        
        else :
            
            print ("Ingrese valores mostrados en pantalla.") 
            
    else:
        
        print("0")
        
        if veces == 1:
        
            opt2 = input(f"No hay cupos libres en {clase}, desea pasarse a la otra clase? (si - no):\n").lower().strip()
        
            if opt2 == "si":
                
                
                if clase == "Asiento normal" :

                    rangoInferior = 30
                    rangoSuperior = 42
                else:
                    
                    rangoInferior = 0
                    rangoSuperior = 30
                operacionAvion(rangoInferior, rangoSuperior, "", 2)
        
        else:
            
            print ("Lo sentimos no nos quedan cupos, el proximos sale en 3 hrs")
    


asientos = []

for i in range (0,42):

    asientos.append(False)

while True:
    print ("1.- Asiento normal \n2.- Asiento VIP")
    
    try:
    
        opt = int(input("\nIngrese la opcion que desea:\n"))
        
        if opt == 1:#Asiento normal
            
            operacionAvion(0,30,"Asiento normal",1)
            
        elif opt == 2:#Asiento VIP
            
            operacionAvion(30,42,"Asiento VIP",1)
            
        elif opt == 3:
            
            print("")
            
        elif opt > 5:
            
            print("Opcion ingresada incorrecta")
            
        #.lower() para que lo ingresado este en minusculas
        #.strip() para que elimine los espacios en caso de que la persona se equivoque
        seguir = input ("Desea volver a ver el menu?: (si - no)").lower().strip()
    
        if seguir != "si":
            
            break
    
    except ValueError:
        print("El valor debe ser entre 1 a 5 ")