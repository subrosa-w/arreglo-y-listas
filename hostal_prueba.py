from funciones import *

menu_activo=True 
opcion_seleccionada=0
lista_de_reservas=[
[100,"juanito","juan soto", 18000],
[100,"juanito","josefa mendez", 18000],
[200,"andrea","andrea gonzales", 12000],
[300,"jose","jose oyarzun", 12000],
]

while menu_activo:
    print("Bienvenido al sistema del motel")
    print("Seleccione una opcion: ")
    print("1.- Guardar eserva")
    print("2.- Buscar reserva")
    print("3.- Mostrar reserva")
    print("4.- Modificar reserva")
    opcion_seleccionada=int(input("Ingrese un numero "))

    if opcion_seleccionada == 1:
        #se crea una nueva lista y se guardan los nuevos pasajeros
        reserva_modificada=guardar_reserva(lista_de_reservas)
        #se actualiza la lista original
        lista_de_reservas=reserva_modificada
        print("Reserva guardada con exito ")

    if opcion_seleccionada == 2:
        buscar_reserva_por_habitacion(lista_de_reservas)

    if opcion_seleccionada == 3:
        mostrar_reserva(lista_de_reservas)

    if opcion_seleccionada == 4:
        print("lol")