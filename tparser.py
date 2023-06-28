import re


#------------------------------Bloque Principal--------------------------------------------------------


def filter_text(file_object): #Función de filtrado del show tech 

    """Esta es la función principal de filtrado. Tiene los patrones fundamentales para filtrar un 
    archivo de show tech"""

    patterns = ["--* show version --*","--* show running-config --*","--* show platform --*",
                "--* show romvar --*","-* show inventory --*","--* show region --*"]
    text = file_object.read()
    matches = []
    borders = []
    substrings = []
    k = 0

    for i in patterns:
        matches.append(re.search(i,text))
    for j in matches:
        borders.append(j.start())

    while k <= len(borders)/2 + 1: #Obtiene porciones del show tech de acuerdo a las fronteras obtenidas
        #Por medio de expresiones regulares
        substrings.append(text[borders[k]:borders[k+1]-1])
        k=k+2
        
    return substrings

def writer(snippet_list,output_file): #Función de escritura de secciones filtradas
    
    for i in snippet_list:
        output_file.write(i)
        output_file.write("\n\n")


#------------------------------Rutinas de ROMMON--------------------------------------------------------


def searchROMMON(text): #Función de extracción de la versión de ROMMON 
    #  Función central para el manejo de la versión de ROMMON 
    patterns = ["R0        [0-9]*            [0-9]{1,2}.[0-9]\([0-9]{1,2}r\)"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))
    
    firmware = matches[0].group()
    match2 = re.search("[0-9]{1,2}.[0-9]\([0-9]{1,2}r\)",firmware) #Removiendo de la línea lo que no tiene
    #que ver con la versión de ROMMON
    number = match2.group()
    #suggested, ROMMON, notes = ROMMON_Validator(number)

    return number

#------------------------------Rutinas de IOS/IOS-XE--------------------------------------------------------


def searchVersion(text): #Función de extracción de la versión de IOS O IOS-XE
   
    patterns = [ "Version [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))

    version = matches[0].group()
    match2 = re.search("[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}",version)
    number = match2.group()
    
    return number
