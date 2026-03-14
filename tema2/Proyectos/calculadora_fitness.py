# ==========================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ==========================================
 
def calcular_imc(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal (IMC).
    
    Fórmula: IMC = peso / (altura^2)
    
    Parámetros:
    peso_kg (float): Peso en kilogramos
    altura_m (float): Altura en metros
    
    Retorna:
    float: El IMC calculado
    """
    return peso_kg / (pow(altura_m/100,2))
    
 
def es_peso_saludable(imc):
    """
    Determina si el IMC está en rango saludable (18.5 - 24.9).
    
    Parámetro:
    imc (float): Índice de Masa Corporal
    
    Retorna:
    bool: True si está en rango saludable, False si no
    """
    # Operadores de comparación y lógicos
    return imc >= 18.5 and imc <= 24.9
 
 
def tiene_sobrepeso(imc):
    """
    Determina si hay sobrepeso (IMC >= 25).
    """
    return imc >= 25
 
 
def tiene_bajo_peso(imc):
    """
    Determina si hay bajo peso (IMC < 18.5).
    """
    return imc < 18.5
 
 
def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.
    Parámetros:
    peso_kg (float): Peso en kg
    altura_cm (float): Altura en cm
    edad (int): Edad en años
    es_hombre (bool): True si es hombre, False si es mujer
    Retorna:
    float: Calorías diarias recomendadas
    """    
    if es_hombre:
        return (88.362 + (13.397 * peso_kg) + (4.799 * altura_cm/100) - (5.677 * edad))
    else:
        return (447.593 + (9.247 * peso_kg) + (3.098 * altura_cm/100) - (4.330 * edad))
    # Operadores aritméticos y booleanos
    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad)
    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad)




    # Usa el hecho de que True=1 y False=0
    # TU CÓDIGO AQUÍ
 
 
def calcular_agua_diaria(peso_kg):
    """
    Calcula litros de agua recomendados al día (35ml por kg de peso).
    """
    return peso_kg * 35 / 1000
 
 
def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo (220 - edad).
    """

    return 220 - edad 



def run():
    # Ejemplo de uso
    print("Este programa proporciona tus insights fitness ")
    peso = int(input("Por favor, introduce tu masa en kg:"))
    altura = int(input("Por favor, introduce tu altura (cm):"))
    edad = int(input("Por favor, introduce tu edad en años:"))
    es_hombre = bool(input("¿Eres hombre? escribe 1 para si, 0 para no: "))
    
    imc = calcular_imc(peso, altura)
    print(f"IMC: {imc:.2f}")   
    print(f"¿Peso saludable? {es_peso_saludable(imc)}")
    print(f"¿Sobrepeso? {tiene_sobrepeso(imc)}")
    print(f"¿Bajo peso? {tiene_bajo_peso(imc)}")
    
    calorias = calcular_calorias_diarias(peso, altura * 100, edad, es_hombre)
    print(f"Calorías diarias recomendadas: {calorias:.2f}")
    
    agua = calcular_agua_diaria(peso)
    print(f"Agua diaria recomendada (litros): {agua:.2f}")
    
    ritmo_maximo = calcular_ritmo_cardiaco_maximo(edad)
    print(f"Ritmo cardíaco máximo: {ritmo_maximo} bpm")

# TU CÓDIGO AQUÍ
#Conceptos importantes
#📌 Booleanos como números (¡MUY IMPORTANTE!)
#En Python, True y False pueden usarse en operaciones matemáticas:

# True + True # 2 (porque True = 1)
# False + False # 0 (porque False = 0)
# True * 100 # 100
# False * 100 # 0

# # Esto es útil para elegir entre dos valores:
# es_adulto = True
# precio = es_adulto * 10 + (1 - es_adulto) * 5
# # Si es_adulto es True: 1*10 + 0*5 = 10
# # Si es_adulto es False: 0*10 + 1*5 = 5

run()