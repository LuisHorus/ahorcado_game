# Importando Librerias choice palabra aleatoria
import random
from random import choice

# Variables
palabras = ["oso", "tigre", "leon", "avestruz", "cocodrilo", "elefante", "jirafa", "tiburon", "zebra", "mono"]
secret_word = random.choice(palabras)
len_word = len(secret_word)
print(secret_word)

def interfaz():
    # Funcion para mostrar Interfaz
    print("==============================================")
    print("========= Ahorcado Game ======================")
    print("==============================================")
    print("_" * len_word)

def dibujos(intentos):
    # Dibujos del Ahorcado donde se validan por intentos
    print("\n")
    if intentos == 4:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {intentos} intentos")
        print(f"""
                            ______________
                            | /          |
                            |/          
                            |              
                            |              
                        """)

    elif intentos == 3:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {intentos} intentos")
        print(f"""
                            ______________
                            | /          |
                            |/          ( )
                            |             
                            |              
                            """)

    elif intentos == 2:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {intentos} intentos")
        print(f"""
                               ______________
                               | /          |
                               |/          ( )
                               |            |  
                               |              
                           """)
    elif intentos == 1:
        print(f"Lo siento fallaste vuelve a intentar - Te quedan {intentos} intentos")
        print(f"""
                               ______________
                               | /          |
                               |/          ( )
                               |            |  
                               |           /    
                           """)

def validar_palabra(intentos=5):
    # Validacion de Palabras y e le pasa 5 vidas
    interfaz()
    letras_erroneas=[]
    while intentos > 0:
        respuesta = input("Escribe una letra: ")
        if len(respuesta) >= 2:
            print('Solo es valido 1 letra vuelve a intentar')
        elif respuesta in secret_word:
            print(f"Adivinaste una palabra {respuesta}")
            return respuesta
        else:
            intentos -= 1
            letras_erroneas.append(respuesta)
            print(f"Letras Erroneas: {letras_erroneas}")
            dibujos(intentos)
    print("Lo siento te haz acabado todas tus vidas")

    print(f"""
                    ______________
                    | /          |
                    |/          ( )
                    |            |  
                    |           / \   
                """)


def main_game():
    # Ejecuta el programa
    correcta = validar_palabra()
    print(f"la palabra correcta es {correcta}")
    return correcta

main_game()
