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
