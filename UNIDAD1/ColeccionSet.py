#SETS

##*Inmutable y mutable a la vez
##*NO PUEDE TENER NUMEROS REPETIDOS
##*SE PUEDEN AGREGAR Y ELIMINAR PERO NO MODIFICAR LOS VALORES
##*Se ordenan automaticamentes
##*ELIMINAN los duplicados, PARA MANEJAR ID's
##*UTILIZAR EN OPERACIONES DE CONJUNTO
##Para declarar un set vacio se debe colocar un 0 dentro de las llaves

# s=set([5,4,3,2,1,0])
# print(s)

##SE ORDENAN LOS VALORES DEL SET
# s={5,4,6,3,8,1}
# print(s)
#
# #SET VACIO
# s={0}

# DECLARACION DE DICCIONARIO
# d={}
# print(type(s))
# print(type(d))

# #NO PUEDE ESTAR UNA LISTA DENTRO DE UN SET
lista=["Mexico", "España"]
a =set(["USA", "Tlaxcala", ("Mexico", "España")])
print(a)

##METODOS

##AGREGAR

s= {2,3,4,5,6,7}
s.add(2)
print(s)

##Eliminar ##BUSCA EL NUMERO SI NO ESTA NO HACE NADA Y SI LO ENCUENTRA LO ELIMINA
s.discard(2)

s.pop()
print()

##LIMPIAR un SET
s.clear()
print(s)


##TEORIA DE CONJUNTOS
s1=(1,2,3)
s2=(3,4,5)

print(s1.union(s2))

##Interseccion va a imprimir el mismo

print(s1.intersection(s2))


## SECUENCIA DE LA INFORMACION ESPECIFICADA PARA LOS PROCESOS DE LA INFOMACION
## SE REALIZARA UN METODO PARA EL FUNCIONAMIENTO CORRECTO DE LA INFORMACION
