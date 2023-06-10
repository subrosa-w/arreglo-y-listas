opcion_multa=input("Su auto tiene alguna multa? Ingrese si o no: ")
if opcion_multa == "si" or opcion_multa == "SI":
    multa_auto=int(input("Ingrese el monto de la multa: "))
    multa_fecha_auto=input("Ingrese la fecha de la multa: ")
elif opcion_multa == "NO" or opcion_multa =="no":
    print("Ha seleccionado que no ")