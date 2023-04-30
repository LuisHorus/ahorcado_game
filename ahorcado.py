# Importando Librerias choice palabra aleatoria
import random
from random import choice

# Variables
palabras = ["oso", "tigre", "leon", "avestruz", "cocodrilo", "elefante", "jirafa", "tiburon", "zebra", "mono"]
secret_word = random.choice(palabras)
len_word = len(secret_word)
letras_correctas = 'abcdefghijklmnñopqrstuvwxyz'



def interfaz():
    # Funcion para mostrar Interfaz
    print("==============================================")
    print("========= Ahorcado Game ======================")
    print("==============================================")
    print("Adivina la palabra oculta ===== Tienes solo 5 Intentos")
    print("Buena Suerte...")
    print(f"""
                                ______________
                                | /          
                                |/          
                                |              
                                |              
                            """)

def dibujos(vidas):
    # Dibujos del Ahorcado donde se validan por intentos
    print("\n")
    if vidas == 4:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {vidas} intentos")
        print(f"""
                            ______________
                            | /          |
                            |/          
                            |              
                            |              
                        """)

    elif vidas == 3:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {vidas} intentos")
        print(f"""
                            ______________
                            | /          |
                            |/          ( )
                            |             
                            |              
                            """)

    elif vidas == 2:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {vidas} intentos")
        print(f"""
                               ______________
                               | /          |
                               |/          ( )
                               |            |  
                               |              
                           """)
    elif vidas == 1:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {vidas} intentos")
        print(f"""
                               ______________
                               | /          |
                               |/          ( )
                               |            |  
                               |           /    
                           """)
    else:
        print("Lo siento te haz acabado todas tus vidas")

        print(f"""
                         ______________
                         | /          |
                         |/          ( )
                         |            |  
                         |           / \   
                     """)

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    oculto=' '.join(lista_oculta)
    return oculto
def mm():
    interfaz()
    vidas = 5
    while vidas >0:
        palabra_elegida = input("Elige una letra: ").lower()
        if palabra_elegida in secret_word:
            print("Adivinaste una Letra")
            letra=mostrar_nuevo_tablero(palabra_elegida)
            print(letra)

        else:
            vidas =vidas -1
            dibujos(vidas)





"""def validar_palabra(intentos=5):
    # Validacion de Palabras y e le pasa 5 vidas
    letras_erroneas = []

    while intentos > 0:
        respuesta = input("Escribe una letra: ")
        if len(respuesta) >= 2:
            print('Solo es valido 1 letra vuelve a intentar')
        else:
            intentos -= 1
            letras_erroneas.append(respuesta)
            print(", ".join(letras_erroneas))
            dibujos(intentos)
    return respuesta
"""
mm()