import tfanalyzer

#Phase 1:Open the file
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r") #Opening the file in reading mode
parsed = open("Parsed Show Tech.txt","w+") #Opening the output file. as the file does not exist, then it is created
#w+ mean the file is in writing (w) and reading mode (+).

#Phase 2: Get sub-strings using regex
result = tfanalyzer.filter_text(showtech) #Returna a list of sub-strings with the desired text snipppets


#Phase 3: Save sub-strings on a text file
tfanalyzer.writer(result,parsed)

#Phase 4: Analyze
parsed.close() #CClosing the file is necesary to open the file with the changes. This requires more research
parsed = open("Parsed Show Tech.txt","r+") #Opening the file in reading (r) and writing mode (+)
text = parsed.read() #Reading output file
version = tfanalyzer.searchVersion(text) #Getting OS version
firmware = tfanalyzer.searchROMMON(text) #Getting ROM version
parsed.write("\n\n")  #tfanalyzer.writer() won't work becase that method will work to print the snippet lists, not a single text line.
parsed.write("---------- Observaciones ----------")
parsed.write("\n\n") #write() method prints a text line on a file object.
parsed.write("\n\n")
    
#Fase 5: Close files to clean system buffer 
showtech.close()
parsed.close()
print("Rutina finalizada con exito")