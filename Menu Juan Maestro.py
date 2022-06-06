from asyncio import exceptions


clientes = [];
opt = 0;

while opt != 4:
    try:
        print("Bienvenido a Juan Maestro: ")
        print("1.- Registrar Cliente")
        print("2.- Suscripcion")
        print("3.- Consultar datos del cliente")
        print("4.- Salir")
        opt = int(input("Ingrese la opcion que desea aplicar: "))

        if opt==1:
            cliente=[]
            run=int(input("Ingrese su rut sin punto ni guion: "))
            if run<=4000000 and run>99999999:
                print("Ingrese un rut valido")
                break
            nombre = input("Ingrese su nombre: ")
            direccion = input("Ingrese su direccion: ")
            comuna = input("Ingrese su comuna: ")
            correo = input("Ingrese su correo: ")
            if "@" not in correo:
                print("Correo debe tener almenos @")
                break
            edad = int(input("Ingrese su edad: "))
            if edad<=0 and edad >110:
                print("La edad debe estar entre 1 y 110 ")
                break
            genero = input("Ingrese su genero: ")
            if genero!="M" and genero !="F" and genero !="O":
                print("Genero deber ser M, F u O ")
                break
            telefono = int(input("Ingrese su celular: "))
            tipo = input("Ingrese tipo de suscripcion: PREMIUM - GOLD - SILVER: ")
            tipo= tipo.upper()
            if(tipo!="PREMIUM" and tipo!="GOLD" and tipo!="SILVER"):
                print("Suscripcion solo pueden ser solo esos 3 tipos: ")
                break
            suscripcion= "suscrito"

            cliente.append(run)
            cliente.append(nombre)
            cliente.append(direccion)
            cliente.append(comuna)
            cliente.append(correo)
            cliente.append(edad)
            cliente.append(genero)
            cliente.append(telefono)
            cliente.append(tipo)
            cliente.append(suscripcion)
            clientes.append(cliente)
            print(clientes)
        if opt==2:
            run=int(input("Ingrese rut de cliente que desea suscribir: "))
            for cliente in clientes:
                if cliente[0] == run:
                    fecha = input("Inserte fecha suscripcion: ")
                    cliente[9]= cliente[9] + "desde\n" + fecha
        if opt==3:
            run=int(input("Ingrese rut de cliente que desea buscar: "))
            for cliente in clientes:
                if cliente[0] == run:
                    print(f"Rut del cliente: {cliente[0]}\n")
                    print(f"Nombre del cliente: {cliente[1]}\n")
                    print(f"Direccion del cliente: {cliente[2]}\n")
                    print(f"Comuna del cliente: {cliente[3]}\n")
                    print(f"Correo del cliente: {cliente[4]}\n")
                    print(f"Edad del cliente: {cliente[5]}\n")
                    if cliente[6]=="M":
                        print("Genero: Masculino\n")
                    if cliente[6]=="F":
                        print("Genero: Femenino\n")
                    if cliente[6]=="O":
                        print("Genero: Otros\n")
                    print(f"Celular del cliente: {cliente[7]}\n")
                    print(f"Tipo de suscripcion del cliente: {cliente[8]}\n")
                    print(f"{cliente[9]}\n")



    except ValueError:
        print("Debe ingresar un valor numerico (1-4)")
    if  opt>4 :
        raise Exception("Opcion debe estar entre 1 y 4")
    