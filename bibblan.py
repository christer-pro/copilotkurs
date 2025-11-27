class Bok:
    def __init__(self,titel,författare,år,pris:float):
        self.titel = titel
        self.författare = författare
        self.år = år
        self.pris = pris

    def info(self):
        return(f"Titel: {self.titel}, Författare: {self.författare}, År: {self.år}, Pris: {self.pris}")
    
bok1=Bok("1984", "George Orwell", 1949, 159.90)
bok2=Bok("To Kill a Mockingbird", "Harper Lee", 1960, 129.50)
print(f"{bok1.info()}\n{bok2.info()}")

bibliotek=[]
bibliotek.append(bok1)
bibliotek.append(bok2)
bibliotek.append(Bok("Brave New World", "Aldous Huxley", 1932, 149.00))
bibliotek.append(Bok("The Great Gatsby", "F. Scott Fitzgerald", 1925, 139.75))
bibliotek.append(Bok("Intr to Python","John Guttag",2021,150))
print(" Böcker i biblioteket")
for bok in bibliotek:
    print(bok.info())
try:
    find_titel=input("Vilken bok vill du söka efter ? ")
    hittad=False
    for bok in bibliotek:
        if bok.titel.lower()==find_titel.lower():
            print("Boken finns i biblioteket:", bok.info())      
            hittad=True
            break
    if not hittad:
        print("Boken finns inte i biblioteket.")
except Exception as e:
    print("Ett fel uppstod vid sökningen:", str(e))

with open("bibliotek.txt", "w", encoding="utf-8") as fil: 
    fil.write("Detta är mitt nya bibliotek")
