try:
    tal=int(input("skriv ett tal: "))
    print("Du skrev talet:",tal)

except ValueError:
    print("Du måste skriva ett giltigt tal.")   

try:
    result=10/0
except ZeroDivisionError:
    print("Du kan inte dela med noll.")

try:
    lista=[1,2,3]
    print(lista[5])
except IndexError:
    print("Index finns inte i listan.")
except ValueError:
    print("Fel värde.") 

