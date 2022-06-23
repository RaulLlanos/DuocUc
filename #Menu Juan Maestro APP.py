#Menu Juan Maestro APP

from logging import exception, raiseExceptions


clientes = []
opt = 0

while opt != 4:
    try:
        cliente= []
        print("1.- Registrar cliente")
        print("2.- Suscripcion")
        print("3.- Consultar datos del cliente")
        print("4.- Salir")
        opt = int(input("Ingrese la opcion que desea: "))

        if opt == 1:
            run = int(input("Ingrese su rut sin digito verificador ni guion:\n"))
            if run < 4000000 and run > 99999999:
                break
            name= input("Ingrese su nombre: \n")
            direction= input("Ingrese su direccion:\n")
            comune= input("Ingrese su comuna:\n")
            email=input("Ingrese su correo: \n")
            if "@" not in email:
                print("Correo debe tener @ ")
                break
            age= int(input("Ingrese su edad: \n"))
            if age <= 0 and age > 110:
                print("La edad debe estar entre 1 y 110")
                break
            gender= input("Ingrese su genero:\n")
            if "M" not in gender and "F" not in gender and "O":
                print("Genero debe ser M, F u O")
                break
            cell= input("Ingrese su numero de contacto: \n")
            kind= input("Ingrese su tipo de suscripcion:\n PREMIUM\n GOLD\n SILVER\n")
            kind= kind.upper()
            if kind!= "PREMIUM" and kind!= "GOLD" and kind!= "SILVER":
                print("Tipo de suscripcion deber estar entre las 3 opciones ")
                break
            suscription= "suscrito"
            
            cliente.append(run)
            cliente.append(name)
            cliente.append(direction)
            cliente.append(comune)
            cliente.append(email)
            cliente.append(age)
            cliente.append(gender)
            cliente.append(cell)
            cliente.append(kind)
            cliente.append(suscription)
            clientes.append(cliente)
            print(clientes)

            if opt == 2:
                run= int(input("Ingrese el run que desea buscar:\n"))
                for cliente in clientes:
                    if cliente [0] == run:
                        fecha=input("Ingrese fecha de suscripcion:\n")
                        cliente[9]= cliente[9] + "desde\n" + fecha
            
            if opt == 3:
                run= int(input("Ingrese el run que desea ver:\n"))
                for cliente in clientes:
                    if cliente[0] == run:
                        print(f"Rut: {cliente[0]}\n")
                        print(f"Nombre: {cliente[1]}\n")
                        print(f"Direccion: {cliente[2]}\n")
                        print(f"Comuna: {cliente[3]}\n")
                        print(f"E-mail: {cliente[4]}\n")
                        print(f"Edad: {cliente[5]}\n")
                        if cliente[6]=="M":
                            print("Genero: Masculino\n")
                        if cliente[6]=="F":
                            print("Genero: Femenino\n")
                        if cliente[6]=="O":
                            print("Genero: Otros\n")

                        print(f"Contacto: {cliente[7]}\n")
                        print(f"Tipo de suscripcion: {cliente[8]}\n")
                        print(f"{cliente[9]}\n")

                    

            
    except ValueError:
        print("Valor erroneo debe digitar segun lo requerido!")
    except TypeError:
        print("Dato erroneo vuelva a intentar!")
    if opt > 4:
        raise Exception("Opcion debe estar entre 1 a 4")