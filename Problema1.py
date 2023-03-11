#Juan Esteban Clavijo García - 202225709
#Problema 1. 

números=[None]*10
a=0

while a!=10:
    x=int(input("Digite un número:"))
    números[a]=x
    a+=1
print("")

limite=int(input("Digite el límite:"))
cma=0
sumacma=0
for elemento in números:
    if elemento<limite:
        cma+=1
        sumacma=sumacma+elemento
mi=min(números)
ma=max(números)
números.sort()

print("")
print("La cantidad de números menores al límite es",cma)
print("La suma de los números menores al límite es",sumacma)
print("Los números ordenados son:",números)
print("El número menor de los 10 valores ingresados es",mi)
print("El número mayor de los 10 valores ingresados es",ma)
