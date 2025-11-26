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
