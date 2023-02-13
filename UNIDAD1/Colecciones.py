###COLECCIONES--TUPLAS 03/02/2023
#Es inmutable(solo si se utilizan metodos se puede mejora/cambiar/modificar)

tupla=(1,2,3)
print(tupla)
tupla=1,2,3
print(type(tupla))
print(tupla)

tupla[0]=5
tupla=1,2,('a','b'),3
print(tupla)
print(tupla[2][0])
tupla=1,2,3
x,y,z=tupla
print(x,y,z)

##DECLARACION DE LAS VARIABLES DE 


##SE MANEJAN LOS VALORES DE SUMA DY RESTA DE LOS VALORES DE LAS SUMAS DE LOS MSDF
##Se maneja con matrices el acceso a los datos

lista=[1,3,2]

##Conversion de lista a tupla
tupla=tuple[lista]

##Convertir de entero a decimal
##PROCESO DE LAS SUMAS DE LOS VALORES PARA SUMAR LOS VALORES DE LASOOS


##Imprimir
for t in tupla:
    print(t)

# ####FUNCIONES(TUPLAS)
#Definir hasta que posicion tome en cienta
l=[1,2,3,4,5,6,7,8,9]
l2=l[0:4]
print(l2)

##Remplazar elementos de la lista principal
l3=[0,0,0]
l[0:3]=l3

##TUPLA CON UN SOLO ELEMENTO
tupla=(2,)
tupla

#Cuantos elementos hay en la tupla
tupla=(2,2,2,2,2,2,2,2,2,2)
print(tupla.count(2))
print(tupla.index(10)) ##No funcionara NO EXISTE el VALOR en la tupla

#Buscar un elemento en la TUPLA
print(tupla.index(3))

##Enviar parametros al index
print(tupla.index(5,5)) ##1: Se refiere al elemento a BUSCAR // 2: Posicion en la que empezara la BUSQUEDA

##Enviar parametros al INDEX
print(tupla.index(5,5))

####COLECCIONES--LISTAS
#Se pueden agregar valores  
lista=[1,2,3]

lista = list("12345")
print(lista)
#Los separa el construct ""listt
lista = [1, "Hola", 3.67, [1,2,3]]
print(lista)

##BUSCAR ELEMENTOS
print(lista(0))
print(lista(-1)) ##Ultimo elemento de la lista

print =(lista)

##Se asigna un nuvo valor a la lusta
lista[3][2]=100 

####FUNCIONES

#Concatenar Estructuras de PYTHON
###Definir hasta que posicion se toma en cuenta

l=[1,3,4,5,6,7,8,9]
l2 =l[0:4]
print(l2)

##Remplazar elementos de la lista principal
l3=[0,0,0]
l[0:3] =l3

#Sumatoria de elementos de
l+=l3
print(l)

##Variables que queremos colocar en la lista
x,y,z =l3
print(x,y,z)

##Recorridos de la lista

lista = [1,2,3,4]
for elemento in lista:
    print(elemento)

##Sacar indices de la lista(posicion)

for index,l in enumerate(lista):
    print(index,l)

#Unir imprimir 2 listas con metodo
lista2=["c","a", "b"]
for  l1, l2 in zip(lista, lista2):
    print(l1,l2)


#Agregar 1 o mas elementos
l=[2,3]


##Generar metodo para crear una lista con un rango 
for i in range [0, len(lista)]:
    print(lista(l))

#Agregar 1 o mas elementos 

l=[2,3]

##Agregar UN ELEMENTO a la lista 
l.append(3)
print(1)

###Agregar ELEMENTOS en MULTITUD
l.extend([1,2,3,4])
print(1)

###INSERTAR en una POSICION ESPECIFICA
l.insert(0,100)
print(l)
e=(100)

###Remover un elemento PERO se debe SABER que EXISTE
l.remov

##Sin ELEMENTO- ELIMINA el ULTIMO
l.pop() 
print(l)

##REVERTIR(VOLTEAR LISTA)
l.reverse()        ##Se llama al metodo REVERSE el cual se va encargar 
print(l)           ##de realiar todo el procedimiento de voltear el orden de la lista


###ORDENAR

##De MENOR a MAYOR (ASCENDENTE)
l.sort()
print(l)

##De MAYOR A MENOR (DESCENDENTE)
l.sort(reverse=True)
print()


l.sort(12)
print(12)


##DECLARACION DE LOS METODOS PARA LOS MODULOS

#MODULO 1:





