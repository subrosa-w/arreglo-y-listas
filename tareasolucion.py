import numpy as np
numero_random=np.random.randint(0,100)
print(numero_random)

x=range(0,10)
arreglo=np.array(x)
for n in x:
    arreglo[n]=np.random.randint(0,100)
print(arreglo)
print("el numero mas grande es: ", arreglo.max() ) 
print("el numero mas pequeño es: ", arreglo.min() )
print("la suma de todos los numeros son :", arreglo.sum())
print("el promedio de todos los elementos son :", arreglo.mean())
