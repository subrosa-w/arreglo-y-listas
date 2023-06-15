#sin argumentos y son retorno
def saludo():
    print("hola")

saludo()
saludo()
saludo() #de esta forma no es necesario escribir print hola para que salude mas de una vez

#Resultado: hola
#           hola
#           hola

#sin argumento y con retorno
def suma():
    num_1=10
    num_2=5
    resultado=num_1+num_2
    return resultado

resultado_suma=suma()
print("\nforma a de utilizar funcion con retorno: ",resultado_suma)
print("forma b de utilizar funcion con retorno: ",suma())
print("forma c de utilizar funcion con retorno: ", suma()+suma())

#con argumentos y sin retorno
def resta1(nume_1, nume_2):
    resultado_1=nume_1-nume_2
    return resultado_1

resultado_10=resta1(10,1)#9
resultado_20=resta1(8,3)#5
#forma decente
print(resultado_10-resultado_20)

#forma bizarra
print(resta1(10,1)+resta1(8,3))#14    