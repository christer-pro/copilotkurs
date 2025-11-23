frukter = ["äpple", "banan", "apelsin"]
print(frukter)

print(frukter[0])  # Första frukten
print(frukter[1])  # Andra frukten
print(frukter[2])  # Tredje frukten

frukter[1] = "päron"  # Ändra andra frukten
print(frukter)  

frukter.append("vindruva")  # Lägg till en frukt
print(frukter)

for frukt in frukter:
    print("Jag gillar", frukt)

färger=["röd", "grön", "blå"]

for färg in färger:
    print("Färgen är", färg)

färger.append("gul")    
print(färger[3])   
