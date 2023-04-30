from random import choice

palabras = ["oso", "tigre", "leon", "avestruz", "cocodrilo", "elefante", "jirafa", "tiburon", "zebra", "mono"]
letras_correctas = []
letras_incorerectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida=input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida):
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidecias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidecias +=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa Letra intenta con otra Diferente")
    else:
        letras_incorerectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidecias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidecias

def perder():
    print("Te has quedado sin vida")
    print("la palabra oculta era "+palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones has encontrado la palabra")

    return True


palabra, letras_unicas=elegir_palabra(palabras)
while not juego_terminado:
    print("====================\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas"+ "-".join(letras_incorerectas))
    print(f"Vidas: {intentos}")
    print("====================\n")
    letra = pedir_letra()
    intentos,terminado,aciertos=chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado
