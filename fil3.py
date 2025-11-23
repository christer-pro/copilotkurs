def hälsa(namn):
    """Hälsar användaren välkommen."""
    print("Hej och välkommen!",namn)

hälsa("Christer")
hälsa("Anna")

def nummer(tal):
    if tal>10:
        print(tal,"är störe än 10")
    
    elif tal==10:
        print(tal,"är lika med 10")
    
    else:
        print(tal,"är mindre än 10")     
    

nummer(2)
nummer(15)  
nummer(10)
