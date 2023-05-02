# Compra de ingredientes para una receta
# Ala secuencia de respuestas (Si - No) se les agrego los strings (strip - capitalize)
print("Recuerda responder (Si) o (No) a todas las preguntas")

print("Primero que todo localiza la tienda mas cercana y ve alla 🏪")
print("--------------------------------------------------------------------------------------------")
print("¿ Hay disponibilidad de los  ingredientes que buscamos ?")
print("                      Si - No")
disponibilidad = input("-").strip().capitalize()

if disponibilidad == "Si":
    print("Excelente , sigamos adelante")    
elif disponibilidad == "No":
    print("No hay problema otro dia seguimos ")
    print("FINNN")
    exit()
else: 
    print ("Por favor ingresa los caracteres recomedados (Si - No)😑")
    print("Vuelve a reiniciar la consola ")
    exit()

# Daremos busqueda a los ingredientes mas frescos    
print("-------------------------------------------------------------------------------------------")
print("¿Estan frescos 🥕?")
print("   Si - No")
frescos = input("-").strip().capitalize()

if  frescos == "Si":
    
    print("Que bien")
    print("Aprovechemos")
elif frescos == "no":
    print("No hay problema otro dia seguimos")
    print("FINNN")
    exit()
else: 
    print ("Por favor ingresa los caracteres recomedados (Si - No)😑")
    print("Vuelve a reiniciar la consola ")
    exit()

# Necesitamos la cantidad exacta , recuerda que hay visista   
print("--------------------------------------------------------------------------------------------")
print("Hay la cantidad necesaria ?")
print("         Si - No")
cantidad = input("-").strip().capitalize()

if cantidad == "Si":
    print("Bien toma los que necesitamos")
elif cantidad == "No":
    print("No hay problema otro dia seguimos")
    print("Recuerda que somos artos")
    print("FINNN")
    exit()
else: 
    print ("Por favor ingresa los caracteres recomedados (Si - No)😑")
    print("Vuelve a reiniciar la consola ")
    exit()

# Recuerda revisar que nos alcanse la plata, no queremos pena 
print("----------------------------------------------------------------------------------------------")
print("Nos alcansa la plata💵 ?")
print("       Si - No")
plata =input("-").strip().capitalize()

if plata =="Si":
    print("Que bien, acercate al cajero con menos fila")
elif plata == "No":
    print("No hay problema otro dia seguimos")
    print("ve pa la casa , no pases pena mejor 😅")
    print("FINNN")
    exit()
else:
    print ("Por favor ingresa los caracteres recomedados (Si - No)😑")
    print("Vuelve a reiniciar la consola ")
    exit()
# Que bien, fue una buena compra
print("-----------------------------------------------------------------------------------------------")
print("Excelente pagaste todo , fue una buena compra")
print("FINN")
exit()

