#print, len, str, int, float

var = "Aprender Python es divertido"

def contar_caracteres(phrase):

    """
    This function returns the length of a phrase using the following format:
    La frase [phrase] tiene [len(phrase)] caracteres."
    
    phrase -- This parameter is a string
    """

    print(f"""La frase {phrase} tiene {len(phrase)} caracteres.""")

def convertir_numero(number):
    number= int(number)
    print(f"Entero: {number}, Tipo: {type(number)}" ) 
    number= str(number)
    print(f"Cadena: {number}, Tipo: {type(number)}" ) 
    number=float(number)
    print(f"Flotante: {number}, Tipo: {type(number)}" ) 

    


contar_caracteres(var)
convertir_numero(42)