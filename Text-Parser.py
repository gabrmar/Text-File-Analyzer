import tparser

#Fase 1: Abrir el archivo
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r") #Apretura del arhivo en modo de lectura
parsed = open("Parsed Show Tech.txt","w+") #Apertura del archivo de salida. como este archivo no existe, entonces
#este archivo será creado de antemano. w+ significa que el archivo está en modo de escritura (w) y lectura (+)

#Fase 2: Obtener las sub-cadenas usando regex
result = tparser.filter_text(showtech) #Regresa una lista de sub-cadenas que se quieren escribir en el archivo de salida


#Fase 3: Grabar las sub-cadenas en un archivo de texto
tparser.writer(result,parsed)

#Fase 4: Analizar
parsed.close() #Cerrar el archivo es necesario para abrir el archivo con lo cambios escritos en el la fase 3. Esto reuire investigación#Closing the file is necesary to open the file with the changes. This requires more research
parsed = open("Parsed Show Tech.txt","r+") #Abriendo archivo en modo de lectura (r) y escritura (+s)
text = parsed.read() #Leyendo archivo modificado
version = tparser.searchVersion(text) #Obteniendo la versión del sistema operativo presente en el archivo de salida
firmware = tparser.searchROMMON(text) #Obteniendo la versión de la ROM presente en el archivo de salida
parsed.write("\n\n")  #No se puede usar tparser.writer() porque fue diseñado para una lista de sub-cadenas
#de caracteres
parsed.write("---------- Observaciones ----------")
parsed.write("\n\n") #el métoo write() en un objeto tipo archivo escribe una línea de texto en un archivo.
parsed.write("\n\n")
    
#Fase 5: Cerrar objetos tipo archivos para limpiar el búffer del systema 
showtech.close()
parsed.close()
print("Rutina finalizada con exito")