# Es una aplicacion que trabaja con cadenas que se ingresan por terminal
# a partir de esto el programa crea tags para usarlo como tags para  videojuegos
# ingreso de nimbre
# apellido
# numero
# Estadisticas
# Nombre completo
# logitud de nombre
# primera letra
# ultima letra


def cabecera():
    """This function creates a shell application header """
    title = r"""
     ____                                _____                ____  ____  ____  
    /  ___| __ _ _ __ ___   ___ _ __     |_   _|_ _  __ _ ___|  _ \|  _ \|  _ \ 
    | |  _ / _` | '_ ` _ \ / _ \ '__|      | |/ _` |/ _` / __| |_) | |_) | |_) |
    | |_| | (_| | | | | | |  __/ |         | | (_| | (_| \__ \  _ <|  _ <|  _ < 
    \____|\__,_|_| |_| |_|\___|_|         |_|\__,_|\__, |___/_| \_\_| \_\_| \_\
                                                   |___/                        
                            
                                『 GαмєяTαɢѕRRR 』
                        🎮 ▬ Crea tu identidad gamer ▬ 🎮
                                ⚡ [ G-T-RRR ] ⚡       
     """
    
    print(title)

# TASKS TO CREATE GAMER TAGS

def crear_tag_basico(nombre):
    """This function creates a basic gamerTag using the first letters at name
    Parameters:
    nombre(str): user's name
    Returns:
    A string of user's name the 4 first characters 
    """
    return nombre[0:4]

def crear_tag_invertido(nombre):
    """This function creates a gamerTag using the reverse user's name
        Parameters:
        nombre(string): User's name

        Returns:
        A reverse string
    """
    return nombre[::-1]

def crear_tag_intercalado(nombre, apellido):
    """This function creates a gamerTag interpoling its name and lastname characters
        Parameters:
        nombre(string): User's name
        apellido(string): User's lastname

        Returns:
        A interpoled user's name 
    """
    print("3. TAG INTERCALADO:",nombre[0:1] + apellido[0:1] + nombre[1:] + apellido[1:])

def create_anagram(name, lastName):
    lengthName = len(name)
    lengthLastName = len(lastName)
    interpolated = ""
    dif=""
    lengthName<lengthLastName if lastName[lengthName:] else name[lengthLastName:]
    for i in range(lengthName):
        interpolated= interpolated + (name+lastName)[i:-(lengthLastName-i-1):lengthName] 
    return interpolated+ dif

def crear_tag_elite(name):
    """
        Crea un gamertag con las ultimas y primeras letras del nombre

        PARAMETRO
        name= nombre del usuario
    """
    print("4. TAG ELITE:",name[0:2], name[-2:], sep="")

def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crear un gamer tag 
    """

    print("5. TAG CON NUMERO: ", nombre[:5], numero_favorito, sep="")


def mostrar_estadisiticas(nombre):
    """
        Muestra estadisticas del nombre proporcionado

        Parametro:
        nombre(str): El nombre a analizar

        Retorna:
        None (imprime directamente)
    """
    print("\nEstadísticas de tu nombre:")
    print("Nombre completo:", nombre)
    print("Longitud nombre:", len(nombre))
    print("Primera letra", nombre[0])
    print("Ultima letra", nombre[-1])

def generar_todas_las_opciones(nombre, apellido, numero):
    """
        Genera y muestra todas las opciones de gamerTags

        Parametros:
        nombre(str): El nombre del usuario
        apellido(str): El apellido del usuario
        numero(str): Es el numero favorito del usuario

        Retorna:
        None (imprime directamente)
    """

    print("""\n============================================================\nTus opciones de gamerTag\n========================================================""")
    
    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BASICO:",tag_basico)

    tag_invertido = crear_tag_invertido(tag_basico)

    print("2. TAG INVERTIDO:",tag_invertido)

    crear_tag_intercalado(nombre,apellido)

    crear_tag_elite(nombre)

    crear_tag_con_numero(nombre, numero_favorito)


cabecera()

nombre = input("\nIngresa tu nombre:")

apellido = input("\nIngresa tu apellido:")

numero_favorito = input("\nIngresa tu numero favorito:")

# MOSTRAR ESTADISTICAS DEL NOMBRE

mostrar_estadisiticas(nombre + " " + apellido)


# Mostrar tags

generar_todas_las_opciones(nombre, apellido, numero_favorito)

print("\n¡Elige tu favorito y conquista el mundo gamer!")



