import numpy as nt

arreglo=nt.array([4,8,15,16,23,42])
contar_hasta=len(arreglo)
for i in range (contar_hasta):
    arreglo[i]=arreglo[i]*2
print(arreglo)

#crear acceso directo a un arreglo
arreglo_copia=arreglo[:]
print("copia: ", arreglo_copia)
#cambio al original
arreglo[0]=3 #cambiamos unas cosas del codigo original
arreglo_copia[2]=100 #distorcionamos un poco el codigo de copia
print("original: ", arreglo)