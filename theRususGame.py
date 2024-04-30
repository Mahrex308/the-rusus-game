# Books xD
"""
Copyright (c) 2024, Marino Olvera Camacho
Todos los derechos reservados.

Fecha de creación: 26/04/2024
Última modificación: 30/04/2024

Descripción: El objetivo es adivinar un numero secreto que la maquina ha seleccionado
             dentro de un rango de numeros que el usuario proporcionara y tiene una 
             cierta cantidad de intentos para lograr adivinarlo. 
"""

import random
import math
import os


def generar_numero(limite_inferior, limite_superior):
    return random.randint(limite_inferior, limite_superior)


def obtener_limite(mensaje):
    while True:
        limite = input(mensaje)
        if limite.isdigit() and int(limite) > 0:
            return int(limite)
        print("Por favor, introduce un numero positivo valido.")


def obtener_intento(mensaje):
    while True:
        intento = input(mensaje)
        if intento.isdigit():
            return int(intento)
        print("Por favor, introduce un numero")


# textos
def ganador():
    # Letrero cuando se gana
    print("+-------------------------------------------------------------------------------------------+")
    print("|***               ඞ                     ඞ                               ඞ               ***|")
    print(r'|***      ______     ______     __   __     ______     ______     ______   ______        ***|')
    print(r'|***     /\  ___\   /\  __ \   /\  -.\ \   /\  __ \   /\  ___\   /\__  _\ /\  ___\       ***|')
    print(r'|***     \ \ \__ \  \ \  __ \  \ \ \-.  \  \ \  __ \  \ \___  \  \/_/\ \/ \ \  __\       ***|')
    print(r'|***      \ \_____\  \ \_\ \_\  \ \_\  \_\  \ \_\ \_\  \/\_____\    \ \_\  \ \_____\     ***|')
    print(r'|***       \/_____/   \/_/\/_/   \/_/ \/_/   \/_/\/_/   \/_____/     \/_/   \/_____/     ***|')
    print("|***                                                                                     ***|")
    print("|***                ඞ                                             ඞ                      ***|")
    print("|***                             [ENTER] para continuar...                               ***|")
    print("|***        ඞ                                                   ඞ                        ***|")
    print("+-------------------------------------------------------------------------------------------+")
    input("|*** ")


def perdedor():
    # Letrero cuando se pierde
    print("+-------------------------------------------------------------------------------------------+")
    print("|***                                                                                     ***|")
    print(r"|***    ______   ______     ______     _____     __     ______     ______   ______       ***|")
    print(r"|***   /\  == \ /\  ___\   /\  == \   /\  __-.  /\ \   /\  ___\   /\__  _\ /\  ___\      ***|")
    print(r"|***   \ \  _-/ \ \  __\   \ \  __<   \ \ \/\ \ \ \ \  \ \___  \  \/_/\ \/ \ \  __\      ***|")
    print(r"|***    \ \_\    \ \_____\  \ \_\ \_\  \ \____-  \ \_\  \/\_____\    \ \_\  \ \_____\    ***|")
    print(r"|***     \/_/     \/_____/   \/_/ /_/   \/____/   \/_/   \/_____/     \/_/   \/_____/    ***|")
    print("|***                                                                                     ***|")
    print("|***                                                                                     ***|")
    print("|***                             [ENTER] para continuar...                               ***|")
    print("|***                                                                                     ***|")
    print("+-------------------------------------------------------------------------------------------+")
    input("|*** ")
                                                                               

def titulo():
    #Aqui todo el titulo
    os.system("cls")
    print("+-------------------------------------------------------------------------------------------+")
    print("|***                                                                                     ***|")
    print("|***                       ██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗                    ***|")
    print("|***                       ██╔══██╗██║   ██║██╔════╝██║   ██║██╔════╝                    ***|")
    print("|***                       ██████╔╝██║   ██║███████╗██║   ██║███████╗                    ***|")
    print("|***                       ██╔══██╗██║   ██║╚════██║██║   ██║╚════██║                    ***|")
    print("|***                       ██║  ██║╚██████╔╝███████║╚██████╔╝███████║                    ***|")
    print("|***                       ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝                    ***|")
    print("|***                                                                                     ***|")
    print("+-------------------------------------------------------------------------------------------+")


def objetivo():
    # Aqui todo el objetivo del juego
    titulo()
    print("|***                                                                                     ***|")
    print("|***                                  OBJETIVO DEL JUEGO                                 ***|")
    print("|***                                                                                     ***|")
    print("|***       Tu objetivo es adivinar un numero secreto que la maquina ha seleccionado      ***|")
    print("|***                 dentro de un rango de numeros que tu proporcionaras.                ***|")
    print("|***                                                                                     ***|")
    print("|***                             [ENTER] para continuar...                               ***|")
    print("|***                                                                                     ***|")
    print("+-------------------------------------------------------------------------------------------+")
    input("|*** ") 


def instrucciones():
    # Aqui todas las instrucciones
    titulo()
    print("|***                                                                                     ***|")
    print("|***                                    ¿COMO JUGAR?                                     ***|")
    print("|***                                                                                     ***|")
    print("|***       1.- Ingresa un limite inferior y un limite superior para establecer el        ***|")
    print("|***        rango en el que se encuentra el numero secreto. Asegurate de ingresar        ***|")
    print("|***                             numeros positivos validos.                              ***|")
    print("|***                                                                                     ***|")
    print("|***       2.- Tendras un numero limitado de intentos para adivinar el numero. El        ***|")
    print("|***       numero de intentos se calcula automaticamente en funcion del rango que        ***|")
    print("|***                                  has establecido.                                   ***|")
    print("|***                                                                                     ***|")
    print("|***       3.- Despues de cada intento, la maquina te dara pistas sobre si el nu-        ***|")
    print("|***          mero que ingresaste es mas alto o mas bajo que el numero secreto.          ***|")
    print("|***                                                                                     ***|")
    print("|***       4.- Continua ingresando numeros y recibiendo pistas hasta que adivines        ***|")
    print("|***                    el numero o hasta que te quedes sin intentos.                    ***|")
    print("|***                                                                                     ***|")
    print("|***       5.- Si adivinas el numero, ¡felicidades, has ganado el juego!                 ***|")
    print("|***                                                                                     ***|")
    print("|***       6.- Si te quedas sin intentos sin adivinar el numero, la maquina reve-        ***|")
    print("|***             lara cual era el numero secreto y habras perdido el juego.              ***|")
    print("|***                                                                                     ***|")
    print("|***                         ¡Diviértete y que empiece el juego!                         ***|")
    print("|***                                                                                     ***|")
    print("|***                             [ENTER] para continuar...                               ***|")
    print("|***                                                                                     ***|")
    print("+-------------------------------------------------------------------------------------------+")
    input("|*** ")


def menu():
    # Aqui van las opciones del menu
    titulo()
    print("|***                                                                                     ***|")
    print("|***                                        MENU                                         ***|")
    print("|***                                                                                     ***|")
    print("|***                                Seleccione una opcion:                               ***|")
    print("|***                                                                                     ***|")
    print("|***                            1. Jugar                                                 ***|")
    print("|***                                                                                     ***|")
    print("|***                            2. Leer el objetivo del juego                            ***|")
    print("|***                                                                                     ***|")
    print("|***                            3. Instrucciones                                         ***|")
    print("|***                                                                                     ***|")
    print("|***                            0. Exit                                                  ***|")
    print("|***                                                                                     ***|")
    print("|***                         [OPCION] + [ENTER] para continuar...                        ***|")
    print("|***                                                                                     ***|")
    print("+-------------------------------------------------------------------------------------------+")


# Program RUSUS
def programa():
    # Aqui esta el programa del juego y la logica
    titulo()
    while True:
        limite_inferior = obtener_limite("|*** Introduce el limite inferior: ")
        limite_superior = obtener_limite("|*** Introduce el limite superior: ")

        if limite_inferior < limite_superior:
            break
        else:
            print("|***  El limite inferior debe de ser menor que el limite superior. Intentelo de nuevo.   ***|")
            

    numero_a_adivinar = generar_numero(limite_inferior, limite_superior)
    intentos = int(math.log2(limite_superior - limite_inferior + 1) + 1)

    print(f"|*** Tienes {intentos} intentos para adivinar el numero entre {limite_inferior} y {limite_superior} ")

    while intentos > 0:
        intento = obtener_intento("|*** Introduce tu numero: ")
        if intento == numero_a_adivinar:
            ganador()
            break
        elif intento < numero_a_adivinar:
            print("|*******************************************************************************************|")
            print("|***                           ¡ATENTO! El numero es mas alto.                           ***|")
            print("|*******************************************************************************************|")
        else:
            print("|*******************************************************************************************|")
            print("|***                           ¡ATENTO! El numero es mas bajo.                           ***|")
            print("|*******************************************************************************************|")
        intentos -= 1
        print(f"|*** ¡CUIDADO! Te quedan solo {intentos} intentos.")
    
    if intentos == 0:
        print(f"|*** ¡Oh no! Te has quedado sin intentos. El numero era {numero_a_adivinar}.")
        perdedor()


def main():
    while True:
        menu()
        opcion = input("|*** ") 
        if opcion == "1":
            programa()
        elif opcion == "2":
            objetivo()
        elif opcion == "3":
            instrucciones()
        elif opcion == "0":
            break
        else:
            print("+-------------------------------------------------------------------------------------------+")
            print("|***             Opcion invalida. Por favor, seleccione una opcion valida.               ***|")
            print("|***                                                                                     ***|")
            print("|***                               [ENTER] para continuar...                             ***|")
            print("+-------------------------------------------------------------------------------------------+")
            input()
        
    
if __name__ == "__main__":
    main()