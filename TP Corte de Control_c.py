import random
import numpy as np
from pyrecord import Record
import os

# Las estructuras de cada uno son las siguientes:
# “CUENTAS”
# Numero_cuenta: Integer;
# Apellido: String [50];
# Nombre: String [50];
# DNI: String [8]
# Tipo_Cuenta: (1 al 15): Integer
# Saldo: Real;
# Activa: Booleano (True=Activa, False=Inactiva dada de baja)
# “CAJEROS”
# Numero_cajero: Integer; (1 al 120)
# Ubicacion: String [50];
# Cant_mov: Integer; (Cantidad histórica de movimientos)

Rcuentas = Record.create_type("Rcuentas","nro_cuenta","apellido","nombre","dni","tipo_cuenta","saldo","activa",                         
nro_cuenta=0,apellido=' ',nombre=' ',dni=' ',tipo_cuenta=0,saldo=0.0,activa=True)

CUENTAS=np.array([Rcuentas]*601)

Rcajeros=Record.create_type("Rcajeros","nro_cajero","ubicacion","cant_mov",
nro_cajero=0,ubicacion=' ',cant_mov=0)

CAJEROS=np.array([Rcajeros]*120)

def carga_cuentas(v):
    a1=open("cuentas.txt","r")
    lectura=a1.readline().strip()
    i=0
    while lectura != "":
        v[i]=Rcuentas()
        s=lectura.split(",")
        v[i].nro_cuenta= int(s[0])
        v[i].apellido=str(s[1])
        v[i].nombre=str(s[2])
        v[i].dni=str(s[3])
        v[i].tipo_cuenta=int(s[4])
        v[i].saldo=float(s[5])
        v[i].activa=bool(s[6])
        if s[6] == "TRUE":
            v[i].sw=True
        else:
            v[i].sw= False                 
        i+=1
        lectura=a1.readline().strip()

    a1.close

def carga_cajeros(v):
    a0=open("cajeros.txt","r")
    lectura=a0.readline().strip()
    i=0
    while lectura!="":
        v[i]=Rcajeros()
        s=lectura.split(",")
        v[i].nro_cajero = int(s[0])
        v[i].ubicacion = str(s[1])
        v[i].cant_mov = int(s[2])
        i+=1
        lectura=a0.readline()
    a0.close()

carga_cuentas(CUENTAS)
carga_cajeros(CAJEROS)

def consulta_cuentas():
    saldo=0
    nro_cuenta=int(input("Ingrese su numero de cuenta para consultar el saldo disponible: "))
    for i in range (601):
        if CUENTAS[i].nro_cuenta == nro_cuenta:
            saldo = CUENTAS[i].saldo
        else:
            i+=1
    print(f"El saldo de la cuenta {nro_cuenta} es {saldo}")

# 2) Procesar el archivo de movimientos, utilizando la técnica de corte de control, para:
# A) Informar el total anual (en $) de los movimientos de cada una de las cuentas.
# B) Informar que cajero registró mayor cantidad de movimientos durante el año.
# C) Actualizar el saldo de las cuentas en CUENTAS.
# D) Actualizar la cantidad de movimientos de cada cajero en CAJEROS

# ARCHIVO “OPERACIONES.TXT” (Secuencial de Texto)
# Número de cuenta: Integer
# Año: Integer
# Mes: Integer
# Día: Integer
# Número de cajero (0 – 119) : Integer
# Tipo de movimiento (1 = depósito, 2 = extracción)
# Monto en pesos: (real)
# El archivo se encuentra ordenado por número de cuenta y dentro de número de cuenta por fecha

def mov_a(v,b):
    total_mov= int(input("Ingrese el numero de cuenta para consultar el total anual de los movimientos: "))-1000
    a0=open("operaciones.txt","r")
    linea=a0.readline().strip()
    s=linea.split(",")
    nro_cuenta = int(s[0])
    vmov=np.array([0]*601)
    i=0
    mayor=0
    mayor_f = 0
    nro_cajeros=np.array([0]*121)
    while linea != "":
        sumatoria=0
        nro_cuenta_actual = nro_cuenta
        while linea != "" and nro_cuenta_actual == nro_cuenta:
            sumatoria+=float(s[6])
            nro_cajeros[int(s[4])]+=1
            if s[5]==1:                        #CONSIGNA C
                v[i].saldo+=float(s[5])
            else:
                v[i].saldo-=float(s[5])
            linea=a0.readline().strip()

            if linea != "":
                s=linea.split(",")
                nro_cuenta = int(s[0])
        vmov[i]=sumatoria
        i+=1
    for t in range (len(nro_cajeros)-1): #Actualizo el vector CAJEROS con la cantidad de movimientos indicadas por el archivo operaciones (PARTE D)
        b[t].cant_mov=nro_cajeros[t+1]
    for x in range(len(vmov)-1):
        if vmov[x]>vmov[x+1] and vmov[x]>=vmov[mayor]: #Busco a la cuenta que realizo el total de movimientos mayor durante el año
            mayor = x
    print(f"El total de movimiento de la cuenta {total_mov+1000} es {vmov[total_mov]}")

    for m in range(len(nro_cajeros)-1):
        if nro_cajeros[m]>nro_cajeros[m+1] and nro_cajeros[mayor_f]<nro_cajeros[m] :
            mayor_f=m
    print("El Cajero que registro mas movimientos en el año es el cajero numero: ", mayor_f) #Consigna B

########################################################################################

# 3) Realizar ABM sobre CUENTAS
# A Altas de nuevas cuentas
# B Borrado de cuentas, solo se pone Activa en False
# M Modificaciones como Apellido, Nombre, DNI y Tipo de cuenta
# - Considerar que cada cliente puede tener solamente 1 cuenta en el banco. Al realizar un alta
# debe verificarse que no exista una cuenta activa para el mismo DNI.
# - La numeración de las nuevas cuentas debe ser consecutiva


# print("Ejecutando la f altas")

def validate(valor):
    while valor < 1000 or valor > 1600:
        print("Valor incorrecto, intente de nuevo.")
        valor = int(input("Ingrese el nro de cuenta:"))
    return valor

def espacio_vector(vec_cuentas, espacio_disponible) -> int: # Funcion para el ejercicio de crear nuevas cuentas.
    espacio_total = len(vec_cuentas) - espacio_disponible

    return espacio_total

def limpiar_pantalla():
    if (os.name)=='posix':
        print()

        input("Presione enter para limpiar..")
        os.system('clear')
    if (os.name)=='nt':
        print()

        input("Presione enter para limpiar..")
        os.system('cls')

def choices(picks) -> int:
    user = int(input("Elija su opción: "))
    while user < 0 or user > picks:
        print("Opción inválida, elija de nuevo.")
        user = int(input("Elija una opción: "))
    
    return user

def validate_acc(choice) -> int:
    while choice < 1 or choice > 15:
        print("Opcion inválida, rango de valores validos: [1-15]")
        limpiar_pantalla()
        choice = int(input("Ingrese un nro de cuenta: "))
        limpiar_pantalla()
    return choice

def dar_de_baja(vec_cuentas):
    suspender_acc = int(input("Elija la cuenta a suspender: "))
    validate(suspender_acc)

    suspender_acc -= 1000

    if vec_cuentas[suspender_acc].activa == True:
        vec_cuentas[suspender_acc].activa = False
        print(f"Nro cuenta: {vec_cuentas[suspender_acc].nro_cuenta}")
        print(f"Apellido: {vec_cuentas[suspender_acc].apellido}")
        print(f"Nombre: {vec_cuentas[suspender_acc].nombre}")
        print(f"DNI: {vec_cuentas[suspender_acc].dni}")
        print(f"Tipo de cuenta: {vec_cuentas[suspender_acc].tipo_cuenta}")
        print(f"Saldo:{vec_cuentas[suspender_acc].saldo}")
        print(f"Estado de cuenta: {vec_cuentas[suspender_acc].activa}")
        print("Cuenta suspendida con éxito.")
    else:
        print("La cuenta ya esta suspendida.")

def dar_de_alta(vec_cuentas, espacio_disponible) -> bool:
    input_dni = input("Ingrese su DNI: ")

    while len(input_dni) != 8:
        input_dni = input("Numero de DNI inválido, intente de nuevo: ")
    
    counter = 0
    found = False
    cant_util = espacio_vector(vec_cuentas, espacio_disponible)

    while counter < cant_util and not found:
        if input_dni == vec_cuentas[counter].dni:
            if vec_cuentas[counter].activa:
                print("La cuenta se encuentra activa.")
                found = True
            else:
                choice = int(input("Ingresar 1 para activar su cuenta, 2 para salir."))

                if choice == 1:
                    vec_cuentas[counter].activa = True
                    found = True
                    print("Cuenta activada con éxito")

        counter += 1
    
    if not found:
        print("Cuenta inexistente, por favor cree una cuenta nueva.")

        cant_util = espacio_vector(vec_cuentas, espacio_disponible)

        vec_cuentas[cant_util] = Rcuentas()
        vec_cuentas[cant_util].nro_cuenta  = cant_util + 1000
        vec_cuentas[cant_util].apellido    = input("Ingrese su apellido: ")
        vec_cuentas[cant_util].nombre      = input("Ingrese su nombre: ")
        vec_cuentas[cant_util].dni         = input_dni
        vec_cuentas[cant_util].tipo_cuenta = int(input("Ingrese su tipo de cuenta: "))
        vec_cuentas[cant_util].saldo       = 0.0
        vec_cuentas[cant_util].activa      = True

        print(f"Cuenta numero {vec_cuentas[cant_util].nro_cuenta} creada con éxito")

def modificar(vec_cuentas):
    cuenta_elegida = int(input("Ingrese el numero de la cuenta a editar: "))
    cuenta_elegida = validate(cuenta_elegida)
    cuenta_elegida -= 1000

    flag = True
    while flag:
        print("1- Editar Apellido")
        print("2- Editar Nombre")
        print("3- Editar DNI")
        print("4- Editar tipo de cuenta")
        print("0- Salir del programa.")

        choice = choices(4)
        if choice == 1:
            vec_cuentas[cuenta_elegida].apellido = input("Ingrese su apelldo: ")
            print("Apellido modificado con éxito.")
            limpiar_pantalla()
        elif choice == 2:
            vec_cuentas[cuenta_elegida].nombre = input("Ingrese el nombre: ")
            print("Nombre modificado con éxito.")
            limpiar_pantalla()
        elif choice == 3:
            vec_cuentas[cuenta_elegida].dni = input("Ingrese el DNI: ")
            while len(vec_cuentas[cuenta_elegida].dni) != 8:
                vec_cuentas[cuenta_elegida].dni = input("Dato inválido, ingrese nuevamente: ")
            print("DNI modificado con éxito.")
            limpiar_pantalla()
        elif choice == 4:
            vec_cuentas[cuenta_elegida].tipo_cuenta = int(input("Ingrese el tipo de cuenta: "))
            vec_cuentas[cuenta_elegida].tipo_cuenta = validate_acc(vec_cuentas[cuenta_elegida].tipo_cuenta)
            print("Tipo de cuenta modificado con éxito.")
        else:
            flag = False


def menu(vec_cuentas):
    flag = True
    while flag:
        print("1- Consultar saldo.")
        print("2- Menú ABM.")
        print("3- Información de cuenta/cajero.")
        print("0- Salir.")

        choice = choices(3)
        if choice == 1:
            consulta_cuentas()
            limpiar_pantalla()
        elif choice == 2:
            menu_abm(vec_cuentas)
            limpiar_pantalla()
        elif choice == 3:
            mov_a(CUENTAS,CAJEROS)
            limpiar_pantalla()
        else:
            flag = False
            print("Programa finalizado...")
            
def menu_abm(vec_cuentas):
    flag = True
    espacio_cuentas = 10
    while flag:
        print("1- Dar de alta una cuenta.")
        print("2- Dar de baja una cuenta.")
        print("3- Modificar una cuenta.")
        print("0- Salir")

        choice = choices(3)
        if choice == 1:
            dni_elegido = dar_de_alta(vec_cuentas, espacio_cuentas)
            limpiar_pantalla()
            if not dni_elegido:
                espacio_cuentas -= 1
        elif choice == 2:
            dar_de_baja(vec_cuentas)
            limpiar_pantalla()
        elif choice == 3:
            modificar(vec_cuentas)
            limpiar_pantalla()
        else:
            flag = False
            print("Saliendo al menú principal...")

menu(CUENTAS)