"GUIA VECTORES: EJERCICIO 1"


import random
import numpy as np

vectorpedido=[0]*250

def cargav(vingresado):

    for i in range (250):

        vingresado[i] = random.randint(-100,100)

    return vingresado

def conteo(vector):

    positivos = 0
    negativos = 0
    ceros = 0

    for n in range (250):

        if vectorpedido[n] > 0:
            positivos += 1

        elif vectorpedido[n] < 0:
            negativos +=1
        
        else:
            ceros +=1

    return positivos, negativos, ceros

def el_mayor_es(vector):

    lenght = len(vector)
    max = -100
    repetidos = 0
    for i in range (lenght):
        if vector[i] > max:
            max = vector[i]
        elif vector[i] == max:
            repetidos += 1
        
    return max, repetidos

def suma_elementos_impares(vector):
    
    sumaimpares = 0
    lenght = len(vector)
    array1 = [0]*(lenght//2)
    n=0
    for i in range (lenght):
        if i % 2 == 1:
            sumaimpares += vector[i]
            array1 [n] = vector[i]
            n += 1
    
    print ("Los Elementos en posiciones impares son: ", array1)
    print ("Suma de Elementos Impares: ", sumaimpares,)



# n = cargav(vectorpedido)
# suma_elementos_impares (vectorpedido)

# print(conteo(vectorpedido))
# print (n)
# mayor, repetido = el_mayor_es(vectorpedido)

# print("el mayor elemento del vector es: ",mayor, "se repite: ", repetido, "veces" )

"GUIA VECTORES: EJERCICIO 2"

#  Definir un array para contener 10 elementos.
# a. Cargar el array con los apellidos de 10 alumnos.
# b. Escribir una función que reciba el vector y un apellido ingresado por teclado y
# retorne True si se encuentra en el vector y False en caso contrario.
# c. Mostrar por pantalla la información indicando si el apellido está o no dentro
# del vector.

apellidos = ["uhg"]*10

def loadSurnames(vec):

    for i in range(10):

        apellido = input("Ingrese un Apellido: ")

        vec[i] = apellido

    return apellidos

def verifico(vec,apellido):

    j = len(vec)
    devuelvo = False

    for i in range(j):
        if vec[i] == apellido:
            devuelvo = True 

    return devuelvo

# loadSurnames(apellidos)

# apellido = input("Ingrese el apellido que busca: ")

# print(verifico(apellidos,apellido))

""" GUIA VECTORES: EJERCICIO 3 """

# 3. Definir un array para contener 5000 elementos.
# a. Cargar el array con 5000 edades (18 a 80) (random)
# b. Realizar una función que indique cual es la edad de mayor frecuencia y su
# frecuencia (la que más se repite y cuántas veces está)

edades = [0]*5000 #CAMBIAR

def cargaredades(vec):
    for i in range(len(vec)-1):
        vec[i] = random.randint(18,80)   #CMABIAR

    print (edades)


def frec(vec):

    aux = 0
    pos = 0
    n = 0

    repeticiones = [0]*63  #CAMBIO [0]*(len(vec)+18)

    for j in range (len(vec)-2):

        for i in range (len(vec)-2):
            

            if vec[j]==vec[i+1] and j != i+1 and n != i+1 and j<i+1:
                n = i + 1
                repeticiones[vec[j]-18] += 1 
    #         print (n, end="  ")
    # print()

    print (repeticiones)

    input("Presione cualquier tecla para ver la edad de mayor frecuencia: ")

    for k in range (len(repeticiones)-1):
        
        if repeticiones[k] >= 1 and repeticiones[k] > aux:

            pos = k
            aux = aux + 1 
    
    print ("La edad de mayor frecuencia es:", pos+18 , "años y se repite:", repeticiones[pos], "veces")


""" def frec(vec):
    inicio = 17

    fcorregido = [0]*5000
    frecuencia = [0]*5018
    for i in range (len(edades)):
        pos = edades[i] 
        frecuencia[pos-1] += 1

    for i in range(5000):
        fcorregido[i] = frecuencia[17+i]

    for i in range(10):

        print(edades[i], end=" ")

    for i in range(10):

        print(fcorregido[i],end=" ") """

# cargaredades(edades)
# frec(edades)


""" GUIA VECTORES: EJERCICIO 4 """

# Definir un array para contener 40 elementos.
# a. Cargar el vector con 40 números entre -10 y 10
# b. Mostrar por pantalla el vector.
# c. Escribir una función que acepte como parámetro el vector y a cada número
# negativo le sume 15 y reemplace el negativo por ese valor.
# d. Mostrar por pantalla el vector modificado.
# e. Escribir una función que reciba el vector anterior, sin negativos y que ante la
# repetición de un número reemplace cada repetición por -1 (menos uno). El
# procedimiento debe retornar el vector modificado y la cantidad de veces que
# fue modificado.
# f. Mostrar por pantalla el vector modificado y la cantidad de veces que fue modificado

contenedor = [0]*10

def cargarv (v):
    for i in range (len(v)-1):
        v[i] = random.randint(-10,10)


input()
cargarv (contenedor)
print (contenedor)
print()

def neg_detector (v):
    for i in range (len(v)-1):
        if v[i] < 0:
            v[i] = v[i] + 15
    
input()
neg_detector(contenedor)
print (contenedor)
print()


def repeticion (v):

    repeticiones = 0
    vaux = [20]*(len(v))
    print("lenght: ", len(v))

    for i in range (len(v)-1):
        for j in range (len(v)-1):
            if v[i] == v[j+1] and i < j+1:
                    vaux[i] = v[i]
                    
    for k in range (len(v)-1):                       
        if vaux[k] != 20:
            for l in range (len(v)):
                if v[l] == vaux[k]:
                    v[l] = -1

    for m in range (len(v)):
        if v[m] == -1:
            repeticiones += 1

    return v, repeticiones

input()
x,y = repeticion(contenedor)

print ("vector modificado sin negativos y con los repetidos como -1: ", x, "se modificó: ", y, "veces")

