# -------------------INTRO PROG1 UNLu PARCIAL 27/10/21--------------------------
# Completar con tus datos:
# Nombre: Joaquin Dominguez
# DNI: 42686593
# Entrega: por GitHub (preferentemente) o por mail a: program1.unlu@gmail.com

# IMPORTANTE: No está permitido usar para resolver el examen estructuras de datos
# o funciones, que no hayamos visto en la materia, o en Introducción a la Programación.

# A) Enumere similaridades y diferencias de búsqueda lineal y búsqueda binaria.

""" Busqueda Lineal y Busqueda Binaria:
Similitudes: ambas dependen del tamaño del vector, requieren de la misma entrada de datos y retornan un lo mismo
Diferencias: 
- La busqueda lineal no necesita de un vector ordenado, mientras que la busqueda binaria si
- La Busqueda lineal debe recorrer todo los elementos de un vector hasta encontrar el elemento deseado o para confirmar que no esta, mientras que el algoritmo de busqueda
binaria hace uso del vector ordenado que recibe como parametro para realizar un menor numero de iteraciones """

# B) Escriba una función en Python que reciba como parámetros dos vectores de
# enteros v1 y v2 de igual longitud, un booleano prim, y RETORNE un vector que
# sea la intercalación de v1 y v2, empezando por v1, si prim es True, y
# empezando por v2 si prim es False.
# Por ejemplo, si prim=True, v1= [1,4,7], v2=[8,0,2] la función debería retornar
# el vector [1,8,4,0,7,2].
# Por ejemplo, si prim=False, v1= [1,4,7], v2=[8,0,2] la función debería retornar
# el vector [8,1,0,4,2,7].
import random
import numpy as np

# Ponele a la función los parámetros que consideres necesarios
def intercalar_Vectores(v1,v2, prim):
    v3 = np.array([0]*(len(v1)*2))
    j = 0
    if prim == True:
        for i in range (len(v3)//2):
            v3[j] = v1[i]
            v3[j+1] = v2[i] 
            j += 2
    if prim == False:
        for i in range (len(v3)//2):
            v3[j] = v2[i]
            v3[j+1] = v1[i] 
            j += 2
    return v3


                # v1= [1,4,7]
                # v2=[8,0,2]
                # prim=False

                # print(intercalar_Vectores(v1,v2,prim))

# C) Escriba una función en Python que reciba como parámetros 1 matriz a de
# m filas y n columnas, y un vector v de longitud n, y retorne una matriz que
# sea el resultado de multiplicar cada columna_i de la matriz a por cada
# elemento_i del vector v.
# Por ejemplo, si la matriz a es:
# 2 3 0
# 1 5 4
# y v=[2,1,0]
# retorna la matriz
# 4 3 0
# 2 5 0


# Ponele a la función los parámetros que consideres necesarios
def multiplo_columna_matriz(matriz, v):
    datos = np.array(np.shape(matriz))
    m = datos[0]   #FILAS
    n = datos[1]   #COLUMNAS
    matriz_retorno = matriz
    for h in range (m):
        for i in range (n-1):
            matriz_retorno[h,i] *= v[i]   #FILAS Y COLUMNAS MATRIZ[F,C]
    
    return matriz_retorno

            # v1= [2,3,0]
            # v2= [1,5,4]
            # matriz = np.array([v1,v2])
            # print(matriz[1,2])
            # v=[2,1,0]
            # print(multiplo_columna_matriz(matriz,v))

# D) Dentro de una empresa de computacion de 5000 empleados, se desea
# conocer cual es  la preferencia de sus empleados respecto al tipo de modalidad
# laboral, Presencial (P), Remota (R) o Mixta (M).

# Además se solicita el sexo y el puesto laboral del encuestado:
# G: Gerente
# P: Programador
# A: Administrativo

# Se nos encargó escribir un programa para ingresar y procesar los datos.
# Para cada empleado censado, se ingresan únicamente los siguientes datos:

# Modalidad: "P", "R" o "M"
# Sexo: "F" o "M" (correspondiente a femenino y masculino respectivamente);
# Puesto laboral: "G", "P", "A".


# Decida la estructura de datos más adecuada para almacenar la información
# del relevamiento de los 5000 empleados, y escriba el programa para la
# carga de datos. IMPORTANTE: No es necesario validar los datos.

# Además, escribir una función que reciba como entrada la estructura de dato
# que contiene la información del censo y un puesto laboral, y retorne
# el tipo de modalidad preferido en dicha categoría de puesto.

modalidad = np.array(["P", "R", "M"])
sexo = np.array(["M", "F"])
puesto = np.array(["G", "P", "A"])
matriz = np.array([[" "*20]*3]*5000)


def load(m, modalidad, gender, puesto_laboral):
    rows, columns = np.shape(m)
    for r in range(rows):
        for c in range (columns):
            if c == 0:
                m[r, c] = random.choice(gender)
            elif c == 1:
                m[r, c] = random.choice(puesto_laboral)
            elif c == 2:
                m [r, c] = random.choice(modalidad)

def show(m):
    rows, columns = np.shape(m)
    for r in range(rows):
        for c in range(columns):
            print(matriz[r, c], end=" ")
        print("")
    print("")


load(matriz, modalidad, sexo, puesto)
show(matriz)

def preferencia(m):
    g=0
    p=0
    a=0
    gp,pp,ap=0,0,0
    gr,pr,ar=0
    gm,pm,am=0
    rows, columns = np.shape(m)
    favg,favp,fava="z","z","z"
    for r in range (rows):
        for c in range (columns):
            if c == 1 and m[r, c] == "G":
                g += 1
                if m[r,2 == "P"]:
                    gp+=1
                elif m[r,2 == "R"]:
                    gr+=1
                else:
                    gm+=1
            elif c == 1 and m[r, c] == "P":
                p+=1
                if m[r,2 == "P"]:
                    pp+=1
                elif m[r,2 == "R"]:
                    pr+=1
                else:
                    pm+=1
            else:
                if m[r,2 == "P"]:
                    ap+=1
                elif m[r,2 == "R"]:
                    ar+=1
                else:
                    am+=1
                a+=1
    if gp > gr and gp > gm:
        favg = "PRESENCIAL"
    elif gr > gp and gr > gm:
        favg = "REMOTO"
    else:
        favg = "MIXTO"
    if gp > gr and gp > gm:
        favg = "PRESENCIAL"
    elif gr > gp and gr > gm:
        favg = "REMOTO"
    else:
        favg = "MIXTO"
