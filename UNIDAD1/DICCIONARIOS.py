##TIENEN UN INDICE, LA LLAVE QUE LE DAMOS A LAS PROPIEDAS
##ANIDADOS
##SE LE PUEDEN MODIFICAR 

d1 = {
    "Nombre":"Rocio",
    "Edad" : 24,
    "documento:" : 232434  ##LA LLAVE DEBE ESTAR ENTRE COMILLAS
}
print(d1)

##CON SU CONSTRUCTOR

d2 = dict((("Nombre", "Rocio"), ("Edad", 24), ("documento", 2345)))
print(d2)

##CON CONSTRUCTOR Y PROPIEDADES

d3 = dict(Nombre="Rocio", Edad=24, documento= 323424)
print(d3)

##METODO GET
##PARA BUSCAR LAS LLAVES
print(d1("Nombre"))
print(d1.get("Nombre"))

# d1["Nombre"] = "Juan"
# print(d1)

# ##AGREGAR AUTOMATICAMENTE
# d1["Direccion"] = "Calle23"
# print(d1)

# ##RECORRIDO DE DICCIONARIOS-- Por cada indice va a iterar
# for x in d1:
#     print(d1(x))

# ##FUNCION PARA ITERAR EL DICCIONARIO--Muestra los valores del 
# for x, y in d1.items():
#     print(x,y)


# d1["obj"]= {"Curp": 1212} ##PRUEBA

# for x, y in d1.items():
#     print(x,y)

# d1 = {"4":1, "b":2}
# d2 = ()

# ##FUNCIONES DE LOS DICCIONARIOS
# d1.clear() ##SI LO EIMPRME VACIO ES VACIO SI IMPRIME UN 0 
# print()

# d = {"a":1, "b":2}
# print(d.get("c"))


# ##METODO ITEMS: REGRESA UNA LISTA ITERABLE
# it = d.items()
# print(it)
# print(list(it))
# print(list(it)(0)(0))

# ##SABER SOLO LLAVES
# k = d.keys()
# print(k)
# print(list(k)(1))

# ##ELIMINAR VALORES CON EL METODO POP

# d.pop("a")
# print(d)
# pop = d.pop("C", -1)
# print(pop) ##Para que no regrese ningun error

# ##ELIMINAR ALGO ALEATORIO DE UN DICCIONARIO

# d.popitem()
# print(d)


# ##UNIR DOS DICCIONARIOS

# d1= {'a':1, 'b':2}
# d2= {'c':233, 'd': 122}
# d1.update(d2) ##EL QUE DOMINA ES EL QUE SE RECIBE COMO PARAMERTRO
# print(d2) ##el d2 es el que domuna
