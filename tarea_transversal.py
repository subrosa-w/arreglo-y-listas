general=0
menu_prin=True
multa_auto=0
multa_fecha_auto=0
precio_auto=0

while menu_prin == True:
    try:
        print("----------Menú Auto Seguro----------\n")
        print("1.- Grabar: \n")
        print("2.- Buscar: \n")
        print("3.- Imprimir Certificados: \n")
        print("4.- Salir: \n")
        opcion_seleccionada=int(input("Seleccione una opcion: "))
        if opcion_seleccionada == 1:
            print("Ha seleccionado la opcion 1.- Grabar: \n")
            tipo_auto=input("Ingrese el tipo de auto: ")
            patente_auto=input("Ingrese la patente del auto: ")
            marca_auto=input("Ingrese la de su marca de auto: ")
            precio_auto=int(input("Ingrese el precio del auto: "))
            opcion_multa=input("Su auto tiene alguna multa? Ingrese si o no: ")
            if opcion_multa == "si" or opcion_multa == "SI":
                multa_auto=int(input("Ingrese el monto de la multa: "))
                multa_fecha_auto=input("Ingrese la fecha de la multa: ")
            elif opcion_multa == "NO" or opcion_multa =="no":
                print("Ha seleccionado que no ")
            fecha_registro_vehiculo=input("Ingrese la fecha de registro del vehículo: ")
            dueño_vehiculo=input("Ingrese el nombre del dueño: ")
            general= tipo_auto, patente_auto, marca_auto, precio_auto, multa_auto, multa_fecha_auto, fecha_registro_vehiculo, dueño_vehiculo
            print(general)

        #//////////////////////////////////////////////////////////////////////////
        if opcion_seleccionada == 2: 
            print("Ha seleccionado la opcion 2.- Buscar: ")
            buscar_patente=int(input("Ingrese la patente del auto para buscar: "))
            if buscar_patente == patente_auto:
                print(general)
            else:
                print("La patente no existe: ")
        #//////////////////////////////////////////////////////////////////////////

        if opcion_seleccionada == 4:
            print("\nHa seleccionado la opcion 4.- Salir: \n")
            print("Version del programa 1.1")
            menu_prin=False
            
    except ValueError:
        print("\nIngrese Numeros enteros: \n")