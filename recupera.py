# ----------------- PROGRAMACION1 UNLu RECUPERATORIO 9/12/21--------------------
# Completar con tus datos:
# Nombre: Joaquin Dominguez
# DNI: 42686593
# Entrega: por GitHub (preferentemente) o por mail a: program1.unlu@gmail.com

# IMPORTANTE: No está permitido usar para resolver el examen estructuras de datos
# o funciones, que no hayamos visto en la materia, o en Introducción a la Programación.

# Escribir un programa que reciba un archivo de texto (MOVI.TXT) y un vector de 
# registros (PRECIOS) y realice lo solicitado en el siguiente enunciado.
       
# Una estación de servicio almacena en un archivo de texto (MOVI.TXT), organizado 
# de modo secuencial, la información diaria de los litros de combustible despachados 
# durante el mes de octubre.
# Cada una de las líneas del archivo MOVI.TXT tienen los siguientes datos, 
# separados por coma:
#     • día (1-31)
#     • hora (0-23)
#     • minutos (0-59)
#     • código_surtidor (1-15)
#     • código_combustible (1-10)
#     • litros_despachados
# El archivo MOVI.TXT se encuentra agrupado y ordenado por día.

# PRECIOS es un vector de REGISTROS de longitud 10 que almacena los precios de 
# los combustibles.
# Los registros del vector PRECIOS tienen la siguiente estructura 
#     • código_combustible (número entero entre 1-10, no se puede repetir)
#     • precio_por_litro (float)
# El vector PRECIOS está ordenado por código_combustible

# Se pide:
# a) Definir la estructura de los registros del vector PRECIOS.
# b) Definir y cargar el vector PRECIOS (los valores de los precios por litros 
# definirlos en forma random)
# c) Escribir un programa que utilizando la técnica del corte de control 
# sobre el archivo MOVI.TXT, muestre por pantalla un informe con los
# litros totales vendidos ese día y su recaudación, y al finalizar, el total del mes.
# Por ejemplo, el informe quedaría de esta forma:
# 		Dia         litros totales           recaudación
# 		  1                568                    $   43200.2
#  		  2                734                    $   87500.5
# 	          .                 .                     $       . 
# 		  .                 .                     $       .
# 		  31               512                    $   50700.9

#     	     Total mes            50000                  $   357800.6
       

# NOTA IMPORTANTE: 
# No es necesario la utilización de ningún otro vector extra para la resolución de 
# este ejercicio.
# El archivo MOVI.TXT debe ser leído una sola vez en todo el programa. 

import numpy as np
from pyrecord import Record
import random

Rprecios = Record.create_type("Rprecios","codigo_combustible","precio_por_litro",        
codigo_combustible=0,precio_por_litro=0.0)                                              # Defino la estructura del Registro Rprecios 

PRECIOS = np.array([Rprecios]*10)                                                       # Defino el vector PRECIOS 


def carga_precios(v,r):                                                                 # Defino la funcion de carga del vector precios
    for i in range(len(v)):
        v[i]=r()
        v[i].precio_por_litro = random.randint(90,120) + random.random()
        v[i].codigo_combustible = i+1                                                   # Como el vector PRECIOS se encuentra ordenado por codigo_cobustible, es cargado con la asignacion

carga_precios(PRECIOS,Rprecios)    # Llamo a la funcion para cargar el Vector precios   # i + 1

def corte(v):                                                                           # Utilizo la tecnica de corte de control para informar la recaudacion y los litros despachados 
    a0=open("MOVI.txt","r")                                                             # en el dia y en total durante el mes 
    line=a0.readline().strip()
    s=line.split(",")
    total_del_mes_litros=0
    total_del_mes_recaudacion=0
    dia = s[0]
    n=0
    print("DIA   Litros Totales   Recaudacion")
    print()
    while line != "":
        dia_ant = dia
        litros_dia=0
        recaudacion_dia= 0
        while line !="" and dia_ant == dia:
            litros_dia += int(s[5])
            for i in range(len(v)):                                                     # Busco en el vector PRECIOS el precio del combustible en particular (1-10) para obtener la 
                if v[i].codigo_combustible == int(s[4]):                                # recaudacion
                    n=i
            recaudacion_dia += litros_dia * v[n].precio_por_litro
            line=a0.readline().strip()
            if line != "":
                s=line.split(",")
                dia = s[0]
        print(f"{dia_ant}      {litros_dia}         $ {recaudacion_dia}")
        total_del_mes_litros += litros_dia
        total_del_mes_recaudacion += recaudacion_dia
    print()
    print(f"Total Mes   {total_del_mes_litros}    $ {total_del_mes_recaudacion}")
    print()
    a0.close()

corte(PRECIOS)
            
