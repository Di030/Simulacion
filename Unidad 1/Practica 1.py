###Simulacion
##Practica 1 unidad 2
#Alumno: Reyes Gutiérrez Diego
semilla=2005
n=4
iteraciones=100
resultados=[]

for _ in range(iteraciones):
    cuadrado=str(semilla**2).zfill(2*n)
    inicio=(len(cuadrado)-n)//2
    semilla=int(cuadrado[inicio:inicio+n])
    resultados.append(semilla)

for i, numero in enumerate(resultados, 1):
    print(f"Número aleatorio {i}:{numero}")