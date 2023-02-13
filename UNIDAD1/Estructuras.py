#Estrucutras de control

#If
a = 4
b= 0
if b!= 0:
    print(a/b)
print(b)

a= 10
if a > 5 and a < 15:
    print("A mayor que 5 menor que 15")

if a > 5 : print("es +5");print("Dentro del 15");print(a*b)


##ANIDADOS

x = 5
if x==5 :
    print("es 5")
else:
    print("NO es 5")


if x== 5:
    print("Es 5")
elif x== 6:
    print("Es 6")
elif x==7:
    print("Es 7")
else: 
    print(x)

##TERNARIO
print("Es 5" if x == 8 else "No es 5")

##LADO IZQ= VERDADERO 
##CENTRO= LA CONDICION
##LADO DER= FALSO

##BANDERA TERNARIA DENTRO DE UNA VARIABLE

a = 10
b = 0
c = a/b if b!=0 else -1


####FOR
#Itera sobre variables secuenciales

for i in "python":
    print(i)

##ARREGLO-MATRIZ
lista = [
    [50, 34, 2]
    [12,4, 5]
    [9, 3, 2]
    ]

for i in lista: ##RECORRIDO DE LA MATRIZ
    for j in i:
        print(j)


##POSICIONES DE RANGO

## RANGO
##ENTRE PARENTESIS HASTA EL NUMERO QUE SE VA A ITERAR



for r in range(6):
    print(r)

for i in range(3,20):
    print(i) ## DEL 5 AL 19

for i in range(5, 20, 2):
    print(i)## INICIO-FIN-SALTO

##SE ROMPE EL CICLO, ENCUENTRA LA "Y" Y S E TERMINA
cadena= "Python"
for letra in cadena:
    if letra=="y":
        print(letra)
        break

##PARA QUE CONTINUE EL CICLO
for letra in cadena:
    if letra =="p":
        continue
    print(letra)


####WHILE

x = 5
while x > 0:
    x-=1
    print(x)

##EN UNA SOLA LINEA

while  x > 0: x-=1; print(x)

##SE PUEDE COLOCAR UN ELSE

x = 5
while x > 0:
    x-=1
    print(x)
else:
    print("Bucle finalizado")
    x=5

while True:
    x-=1
    print(x)
    if x ==0:
        break
else:
    print("fin del mundo")


z =7
x = 1
while z >0:
    print(' ' +z '*' * x * ' ' * z)

    

##POSICIONES DE RANGO DE LOS VALORES DE LAS

##ASI DEBE APARECER EL HORARIO DE LAS CONSULTAS DE INFORMACION DE LOS VALORES DE LA BASE DE DAROS DE 