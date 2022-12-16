import json
import random

# #########
# Funciones
# #########


def crear_persona():
    '''Función para generar de una persona'''
    # Creamos un nombre y apellido escrita por teclado.
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    # Teléfono generado aleatoriamente
    tlfno = ""
    for i in range(9): tlfno += str(random.randint(1,9))

    # Cod. Postal generado aleatoriamente
    cod_postal = []
    for i in range(5): cod_postal.append(random.randint(0,5))
    #Creamos un correo electronico a partir del nombre y apellidos escritos por teclado
    gmail = "@gmail.com"
    corr_elec = nombre + "." + apellido + str(random.randint(0,100)) + gmail

    # Devolvemos persona.
    ret = {"nombre" : nombre,
            "apellidos" : apellido,
            "tlfno" : tlfno,
            "Codigo Postal" : cod_postal, 
            "Direccion de correo electronico" : corr_elec}
    return ret


def crear_personas(numero_personas):
    '''Función que devuelve una estructura de personas'''

    ret = {'personas' : None}
    personas = []
    for i in range(numero_personas): personas.append(crear_persona())
    ret['personas'] = personas

    return ret

def f_cargar():
    '''Funcion para cargar los datos de un archivo json'''

    f = open("datos.json", "r")
    personas = json.load(f)
    f.close()
    return personas

def f_guardar(personas):
    '''Funcion para guardas los datos de un archivo json'''
    f = open("datos.json", "w")
    json.dump(personas, f)
    f.close()
    return None

# ##############################
# Código del programa principal.
# ##############################

datos = crear_personas(1) # Creamos varias personas ficticias.

# Abrimos fichero.
f = open("datos.json", "w")

# Volcamos datos de las personas creadas.
json.dump(datos, f)

# Guardamos el fichero.
f.close()

# Ahora vamos a cargar el fichero guardado en memoria.

f = open("datos.json", 'r') # Abrimos el fichero en modo de lectura.
d = json.load(f) # Cargamos datos del fichero abierto.
f.close() # Cerramos el fichero.

# Visualizamos los datos.
print(d)