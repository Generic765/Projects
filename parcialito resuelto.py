# ---------------INTRO PROG UNLU: EJEMPLO PARCIALITO ENUNCIADO------------------
# Completar con tus datos:
# Nombre: Joaquin Dominguez
# DNI: 42686593
# Entrega: por GitHub (preferentemente) o por mail a: introprog.unlu@gmail.com 

# A) Suponé que es necesario escribir un programa que procese la edad de los
# docentes de una universidad, y el programa debe terminar cuando el usuario
# ingresa -99 como edad. ¿Qué estructura repetitiva utilizarías para implementar
# el algoritmo? ¿Por qué?.
# Puntaje: 1/10

""" Emplearia la estructura repetitiva ´while´ para implementar en el algorito 
ya que esta me permite repetir el algoritmo indefinidamente hasta que se ingrese 
el valor -99 para salir del loop."""

# B1) Programar la función suma_primeros_impares que recibe un número natural n
# como parámetro, y retorna la suma los primeros n números impares.
# Ejemplo: si n=3, la función debe retornar 9 (ya que 1+3+5=9) 
# Puntaje: 3/10

# B2) Programar la función test_suma_primeros_impares que testea la función
# suma_primeros_impares, con al menos 2 casos de test. Justifique por qué
# considera que esos casos de tests son relevantes para testear el programa.
# Puntaje: 0.5/10

# C1) Programar la función censo_mails que permita realizar una encuesta sobre
# cuántos emails diarios envían las personas. La función debe permitir hacer la
# encuesta para diez (10) personas, solicitando al usuario ingresar los datos
# por teclado. Además de la cantidad de emails diarios, se debe solicitar la
# edad del encuestado.
# Por ejemplo, una entrada válida del programa sería el valor 15 para la
# cantidad de emails diarios enviados, y 23 para la edad.

# Una vez procesadas las diez personas, la función debe informar por pantalla:
# 1) La edad de la persona que más emails envía por día.
# 2) Si la cantidad de emails del primer encuestado se repite al menos una vez.
# 3) El promedio total de emails diarios enviados entre todos los encuestados.
# Puntaje: 5/10

# C2) ¿Es posible testear que su programa funciona correctamente ingresando
# menos de 10 encuestas? Justifique su respuesta.
# Puntaje: 0.5/10

""" No es posible testar el programa con menos de 10 encuestas debido a que el mismo exije de las mismas para su funcionamiento  """ 
# ------------------------------------------------------------------------------

#################################################
# Funciones Principales y Auxiliares
#################################################

# Ponele a la función los parámetros que consideres necesarios
def suma_primeros_impares(n):
    if n != 0 and n != 1:
        i = 1
        sumaImpares = 1
        total = 1
        while i != n:
            sumaImpares += 2
            total += sumaImpares
            i+=1
        valorfinal = total
    elif n ==0:
        valorfinal = 0
    else: 
        valorfinal = 1
    return valorfinal
    

# Ponele a la función los parámetros que consideres necesarios
def censo_mails():

        Edad1 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios1 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad2 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios2 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad3 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios3 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad4 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios4 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad5 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios5 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad6 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios6 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad7 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios7 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad8 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios8 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad9 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios9 = int(input("¿Cuantos emails envias diariamente?:   "))

        Edad10 = int(input(("¿Cuántos años tienes?:   ")))
        MailsDiarios10 = int(input("¿Cuantos emails envias diariamente?:   "))

        listaedades = [Edad1,Edad2,Edad3,Edad4,Edad5,Edad6,Edad7,Edad8,Edad9,Edad10]
        listamails = [MailsDiarios1,MailsDiarios2,MailsDiarios3,MailsDiarios4,MailsDiarios5,MailsDiarios6,MailsDiarios7,MailsDiarios8,MailsDiarios9,MailsDiarios10]

        masemailsenviados = max(listamails)
        n = listamails.index(masemailsenviados)
        edad_mas_mails_enviados = listaedades[n]

        lista_emails_renew = [MailsDiarios2,MailsDiarios3,MailsDiarios4,MailsDiarios5,MailsDiarios6,MailsDiarios7,MailsDiarios8,MailsDiarios9,MailsDiarios10]
        if MailsDiarios1 in lista_emails_renew:
             repeticion = "SE REPITE AL MENOS UNA VEZ LA CANTIDAD DE EMAILS ENVIADOS DEL PRIMER ENCUESTADO"
        else:
            repeticion = "no se repite la cantidad de mails enviados por el primer encuestado"

        promedio_emails_enviados = sum(listamails)/10

        return  "la edad de la persona que mas emails envia por dia es:  "+ str(edad_mas_mails_enviados) + "El promedio de emails enviados es:  " + str(promedio_emails_enviados) + "     " + repeticion


#################################################
# Funciones de Test
#################################################


def test_suma_primeros_impares():
    print("Testeando suma_primeros_impares... ", end="")
    assert suma_primeros_impares(3) == 9
    assert suma_primeros_impares(1) == 1
    assert suma_primeros_impares(0) == 0
    assert suma_primeros_impares(5) == 25
    print("Pasó!")

    """ Considero a estos casos relevantes porque permiten la observacion de los que sucede en los casos particualres de n==0 y n==1, ademas de corroborar que n==3 retorne 9.
    Adicionalmente agrege un cuarto caso para comprobar el que el algoritmo funciona con n1 != 3 """

#################################################
# Principal
#################################################


test_suma_primeros_impares()
print(censo_mails())
