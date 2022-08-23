import os
titulo = "*Bienvenido al cajero automatico Anyeudi Company (Estamos para ti :)*"
print(titulo)
print(len(titulo) * "=")
usuario = "admin"
contrasena = "1234"
saldo = int(15365)
deposito = 0
deposito1 = 0
a = 0

usuario_1 = input("Ingrese su usuario: \n")
contrasena_1 = input("ingrese su contraseña:\n")


if usuario_1 == usuario and contrasena_1 == contrasena:
    print("A ingresado correctamente!")
    input("presione enter para continuar\n")
    os.system('cls')

    def menu():

        os.system('cls')
        print("Selecciona una opción")
        print("\t1 - Retirar efectivo")
        print("\t2 - Consultar saldo de la cuenta")
        print("\t3 - Depositar a la cuenta ingresada")
        print("\t4 - Comprar recarga")
        print("\t5 - salir")


    while True:

        menu()

        # solicitar una opción al usuario
        opcionMenu = input("inserta el numero de su opcion a elegir >> ")

        if opcionMenu == "1":
            print("¿Que cantidad de dinero desea retirar?")
            a = int(input())
            if a < saldo:
                print('La cantidad de dinero retirada es:' , a)
            else:
                print("no tienes sufuciente balance")
            input("\npulsa cualquier tecla para volver al menu")

        elif opcionMenu == "2":
            print("Su saldo actual es de: ", (saldo + deposito1 - a))
            input("\npulsa cualquier tecla para volver al menu")


        elif opcionMenu == "3":
            print("¿Que cantidad de dinero desea depositar?")
            deposito1 = int(input())
            print("Su saldo depositado es:" , deposito1)
            input("\npulsa cualquier tecla para volver al menu")

        elif opcionMenu == "4":
            print("¿De que compañia desea insertar la recarga?:")
            def menu():
             os.system('cls')
            print("\t1 - Claro")
            print("\t2 - Altice")
            print("\t3 - Viva")
            compania = int(input())
            if compania == 1:
                compania = "claro"
            elif compania == 2:
                compania = "Altice"
            elif compania == 3:
                compania = "Viva"
            valor = int(input("Digite el valor de la recarga "))
            numero = int(input("Ingrese su numero telefonico de {} (Sin guiones) ".format(compania)))
            print("<<Recarga confirmada>>")
            print("El numero telefonico insertado es:",numero, "y el monto recargado es:",valor)
            print("El numero de la recarga es: ")
            import random
            print(random.randrange(1 + 99999))
            input("\npulsa cualquier tecla para volver al menu")

        elif opcionMenu == "5":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
else:
    print("El usuario no a sido encontrado")