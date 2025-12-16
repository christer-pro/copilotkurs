import json
import os

class Bok:
    def __init__(self, titel, författare, år, pris: float):
        self.titel = titel
        self.författare = författare
        self.år = år
        self.pris = pris

    def info(self):
        return f"Titel: {self.titel}, Författare: {self.författare}, År: {self.år}, Pris: {self.pris:.2f} kr"


# --- Funktioner för biblioteket ---

def lista_böcker(bibliotek):
    if not bibliotek:
        print("📭 Biblioteket är tomt.")
        return
    print("📚 Böcker i biblioteket:")
    for bok in bibliotek:
        print("-", bok.info())


def lägg_till_bok(bibliotek):
    titel = input("Titel: ").strip()
    författare = input("Författare: ").strip()
    try:
        år = int(input("År (t.ex. 1949): ").strip())
        pris = float(input("Pris (t.ex. 159.90): ").strip())
    except ValueError:
        print("❌ Ogiltigt år eller pris. Försök igen.")
        return
    ny_bok = Bok(titel, författare, år, pris)
    bibliotek.append(ny_bok)
    print("✅ Bok tillagd:", ny_bok.info())


def ta_bort_bok(bibliotek):
    titel = input("Vilken titel vill du ta bort? ").strip()
    for i, bok in enumerate(bibliotek):
        if bok.titel.lower() == titel.lower():
            print("🗑️ Tar bort:", bok.info())
            del bibliotek[i]
            return
    print("❌ Boken finns inte i biblioteket.")


def sök_bok(bibliotek):
    titel = input("Vilken bok vill du söka efter? ").strip()
    for bok in bibliotek:
        if bok.titel.lower() == titel.lower():
            print("✅ Hittad:", bok.info())
            break
    else:
        print("❌ Boken finns inte i biblioteket.")


# --- Sorteringsfunktioner ---

def sortera_efter_år(bibliotek):
    sorterat = sorted(bibliotek, key=lambda bok: bok.år)
    print("📚 Böcker sorterade efter år:")
    for bok in sorterat:
        print("-", bok.info())


def sortera_efter_pris(bibliotek, stigande=True):
    sorterat = sorted(bibliotek, key=lambda bok: bok.pris, reverse=not stigande)
    print("📚 Böcker sorterade efter pris:")
    for bok in sorterat:
        print("-", bok.info())


def sortera_efter_år(bibliotek, stigande=True):
    sorterat = sorted(bibliotek, key=lambda bok: bok.år, reverse=not stigande)
    print("📚 Böcker sorterade efter år:")
    for bok in sorterat:
        print("-", bok.info())


# --- Spara/Läsa JSON ---

def spara_json(bibliotek, filnamn="bibliotek.json"):
    with open(filnamn, "w", encoding="utf-8") as f:
        json.dump([bok.__dict__ for bok in bibliotek], f, ensure_ascii=False, indent=2)
    print(f"💾 Sparat {len(bibliotek)} böcker till {filnamn}.")


def läs_json(filnamn="bibliotek.json"):
    try:
        with open(filnamn, "r", encoding="utf-8") as f:
            data = json.load(f)
        bibliotek = [Bok(**bok) for bok in data]

        # Bekräfta antalet böcker
        print(f"✅ Läste in {len(bibliotek)} böcker från {filnamn}")

        # Lista böckerna snyggt
        for bok in bibliotek:
            print("-", bok.info())

        return bibliotek

    except FileNotFoundError:
        print(f"❌ Filen {filnamn} hittades inte.")
        return []
    except json.JSONDecodeError:
        print(f"❌ Filen {filnamn} innehåller ogiltig JSON.")
        return []


# --- Meny ---

def huvudmeny():
    print("\n--- Bibliotekssystem ---")
    print("1. Lista böcker")
    print("2. Lägg till bok")
    print("3. Ta bort bok")
    print("4. Sök bok")
    print("5. Sortera efter år")
    print("6. Sortera efter pris")
    print("7. Sortera efter titel")
    print("8. Spara till JSON")
    print("9. Läs från JSON")
    print("10. Avsluta")


def starta_program():
    bibliotek = [
        Bok("1984", "George Orwell", 1949, 159.90),
        Bok("To Kill a Mockingbird", "Harper Lee", 1960, 129.50),
        Bok("Brave New World", "Aldous Huxley", 1932, 149.00),
        Bok("The Great Gatsby", "F. Scott Fitzgerald", 1925, 139.75),
    ]

    while True:
        huvudmeny()
        val = input("Välj (1-10): ").strip()
        if val == "1":
            lista_böcker(bibliotek)
        elif val == "2":
            lägg_till_bok(bibliotek)
        elif val == "3":
            ta_bort_bok(bibliotek)
        elif val == "4":
            sök_bok(bibliotek)
        elif val == "5":
            ordning = input("Stigande (s) eller fallande (f)? ").lower()
            sortera_efter_år(bibliotek, stigande=(ordning == "s"))
        elif val == "6":
            ordning = input("Stigande (s) eller fallande (f)? ").lower()
            sortera_efter_pris(bibliotek, stigande=(ordning == "s"))
        elif val == "7":
            sortera_efter_titel(bibliotek)
        elif val == "8":
            spara_json(bibliotek)
        elif val == "9":
            bibliotek = läs_json()
        elif val == "10":
            print("👋 Avslutar. Tack för idag!")
            break
        else:
            print("❌ Ogiltigt val. Försök igen.")


if __name__ == "__main__":
    starta_program()
