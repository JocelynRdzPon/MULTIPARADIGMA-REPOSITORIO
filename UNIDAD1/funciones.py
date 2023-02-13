# for key: value in kwargs.items();
#     print(key, value)
#     suma == value
# return suma

# print(suma(b=2, c=5, a=4))

# def suma(**kwargs):
#  suma = 0
#  for key , value in kwargs.items():
#     print(key, value)
#     suma += value
# return suma, media, 10
# print(sumaMedia(1,2,3))
# SumaResultado, sumaResultadoMedia, s


##CLASE 12/FEB/2023

##LAMBDAS
"""
se pueden definir como funciones ocultas, privadas

"""
lambda * n: print(sum(n)) (*list(range(0,101,1))) #Es una funcion para realizar procesos pero que se escriben en una sola linea de codigo

"""
Se pueden realizar funciones sin necesidad de ocupar mas de 3 renglones para su ejecucion
"""
"""
"""

def miFuncionSuma(a,b):
    """
    Descripcion util de la funcion, como debe ser usada, que parametros
    """
    return a+b
help(miFuncionSuma)
# print(miFuncionSuma:__doc__)

var= 10

def Multiplicar(numero: int) ->int:
    return numero * 3

print(Multiplicar("5.8"))

def funcion(a,b,*args,**kwargs):
    print(a)
    print(b)
    for arg  in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

funcion(10,2,3,4,5,6,7,8,8, )
##

##IMPRIMIR NUMEROS DEL 1 AL 100 Y SUMARLOSNTR
numeros = list(range(1,101,1))
print(numeros)
def suma(*numeros):
    suma = 0
    for n in numeros:
        suma+=n
    return suma
print(suma(*numeros))
    


##DEVOLVER 2 VALORES

def sumaMedia(a,b,c):
    suma = a + b + c
    media = suma/3
    return suma, media
print(sumaMedia(1,2,3))
sumaResult
