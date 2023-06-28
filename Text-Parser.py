import tparser

#Phase 1:Open the file
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r") #Opening the file in reading mode
parsed = open("Parsed Show Tech.txt","w+") #Opening the output file. as the file does not exist, then it is created
#w+ mean the file is in writing (w) and reading mode (+).

#Fase 2: Get sub-strings using regex
result = tparser.filter_text(showtech) #Returna a list of sub-strings with the desired text snipppets


#Fase 3: Save sub-strings on a text file
tparser.writer(result,parsed)

#Fase 4: Analyze
parsed.close() #Cerrar el archivo es necesario para abrir el archivo con lo cambios escritos en el la fase 3. Esto reuire investigación#Closing the file is necesary to open the file with the changes. This requires more research
parsed = open("Parsed Show Tech.txt","r+") #Opening the file in reading (r) and writing mode (+)
text = parsed.read() #Reading output file
version = tparser.searchVersion(text) #Getting OS version
firmware = tparser.searchROMMON(text) #Getting ROM version
parsed.write("\n\n")  #tparser.writer() won't work becase that method will work to print the snippet lists, not a single text line.
parsed.write("---------- Observaciones ----------")
parsed.write("\n\n") #write() method prints a text line on a file object.
parsed.write("\n\n")
    
#Fase 5: Close files to clean system buffer 
showtech.close()
parsed.close()
print("Rutina finalizada con exito")