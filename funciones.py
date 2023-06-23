def guardar_reserva(lista_de_reservas):
    print("Selecciono la opcion 1: ")
    cantidad_personas=int(input("Ingrese la cantidad de personas a hospedar: "))
    #validar la cantidad de personas que se puedes hospedar en habitacion (maximo 3 personas)


    habitaciones=int(input("Ingrese la habitacion: "))
    nombre_reserva=input("Ingrese el nombre de la reserva: ")
    precio=cantidad_personas*10000

    for n_persona in range(cantidad_personas):
        nombre_pasajeros=input("Ingrese el nombre del pasajero: ")
        lista_de_reservas.append([habitaciones,nombre_reserva,nombre_pasajeros,precio])
    return lista_de_reservas


def buscar_reserva_por_habitacion(lista_de_reservas):
    print("Selecciono la opcion 2: ")
    habitacion_buscada=int(input("ingrese el numero de la habitacion: "))
    largo_lista=len(lista_de_reservas)
    #imprimir toda la lista
    posicion_reserva_en_la_lista=-1

    mensaje="la habitacion esta vacia"
    #recorrer toda la lista
    for fila in range (largo_lista):
        print("Impreso automaticamente", lista_de_reservas[fila])
        reserva_encontrada=lista_de_reservas[fila]
        numero_habitacion_encontrada=reserva_encontrada[0]
        if habitacion_buscada == numero_habitacion_encontrada:
            mensaje="Habitacion reservada"
            posicion_reserva_en_la_lista=fila

    print(mensaje)
    return posicion_reserva_en_la_lista

def mostrar_reserva(lista_de_reservas):
    print("Selecciono la opcion 3: ")
    habitacion_encontrada=buscar_reserva_por_habitacion(lista_de_reservas)
    #si encontre la habitacion ocupada
    if habitacion_encontrada >= 0:
        print("la reserva es: ", lista_de_reservas[habitacion_encontrada])
        