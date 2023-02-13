##MODULOA: Son librerias que se pueden utilizar

import random as ran
import csv as csv


numRandom = ran.randiant(0,100)

while True:
    num = int (input("CUal sera el numero entre 0 y 1000?"))
    if num==numRandom:
        break
    if numRandom > num:
        print("El numero es mayor")
    else:
        print("El numero es menor")

print("El numero era", num)


## MANEJAR ARCHIVOS EXCEL
with open("sample.csv") as file:
    reader = csv.reader(file)
for row in reader:
    print(",".join)