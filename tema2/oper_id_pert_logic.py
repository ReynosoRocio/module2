def adivinar_palabra(letra_prueba, palabra_intento):
    palabra_adivinar = "gelatina"
    palabra_adivinar = palabra_adivinar.upper()
    letra_prueba = letra_prueba.upper()
    palabra_intento = palabra_intento.upper()
    letra_en_palabra = letra_prueba in palabra_adivinar
    resultado_adivinanza = len(palabra_adivinar) == len (palabra_intento) and palabra_intento == palabra_adivinar

    print( f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}.")
    
    print(f"El jugador gana: {resultado_adivinanza}.")




letra_input = input("Este programa es un juego para adivinar una palabra, ingresa una letra: ")

palabra_input = input("Ingresa la palabra: ")

adivinar_palabra(letra_input, palabra_input)