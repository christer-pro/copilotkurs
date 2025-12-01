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

    def __eq__(self, other):
        if not isinstance(other, Bok):
            return NotImplemented
        return (self.titel, self.författare, self.år, self.pris) == (
            other.titel, other.författare, other.år, other.pris
        )


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
        print("❌ Ogiltigt år eller pris. Försök igen med siffror.")
        return
    ny_bok = Bok(titel, författare, år, pris)
    bibliotek.append(ny_bok)
    print("✅ Bok tillagd:", ny_bok.info())


def ta_bort_bok(bibliotek):
    titel = input("Vilken titel vill du ta bort? ").strip()
    # Ta bort första matchande bok med den titeln (skonsamt för tusentals böcker)
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


def spara_json(bibliotek, filnamn="bibliotek.json"):
    try:
        with open(filnamn, "w", encoding="utf-8") as f:
            # __dict__ ger ett uppslagsverk (dict) av objektets fält
            data = [bok.__dict__ for bok in bibliotek]
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Sparat {len(bibliotek)} böcker till {filnamn}.")
    except Exception as e:
        print("❌ Kunde inte spara:", e)


def läs_json(filnamn="bibliotek.json"):
    if not os.path.exists(filnamn):
        print("ℹ️ Ingen fil hittades. Startar med tomt bibliotek.")
        return []
    try:
        with open(filnamn, "r", encoding="utf-8") as f:
            data = json.load(f)
        bibliotek = []
        for item in data:
            # Säker konvertering av typer
            titel = item.get("titel", "")
            författare = item.get("författare", "")
            år = int(item.get("år", 0))
            pris = float(item.get("pris", 0.0))
            bibliotek.append(Bok(titel, författare, år, pris))
        print(f"📥 Läste in {len(bibliotek)} böcker från {filnamn}.")
        return bibliotek
    except Exception as e:
        print("❌ Kunde inte läsa filen:", e)
        return []


def huvudmeny():
    print("\n--- Bibliotekssystem ---")
    print("1. Lista böcker")
    print("2. Lägg till bok")
    print("3. Ta bort bok")
    print("4. Sök bok")
    print("5. Spara till JSON")
    print("6. Läs från JSON")
    print("7. Avsluta")


def starta_program():
    # Startdata (valfritt)
    bibliotek = [
        Bok("1984", "George Orwell", 1949, 159.90),
        Bok("To Kill a Mockingbird", "Harper Lee", 1960, 129.50),
        Bok("Brave New World", "Aldous Huxley", 1932, 149.00),
        Bok("The Great Gatsby", "F. Scott Fitzgerald", 1925, 139.75),
    ]

    while True:
        huvudmeny()
        val = input("Välj (1-7): ").strip()
        if val == "1":
            lista_böcker(bibliotek)
        elif val == "2":
            lägg_till_bok(bibliotek)
        elif val == "3":
            ta_bort_bok(bibliotek)
        elif val == "4":
            sök_bok(bibliotek)
        elif val == "5":
            spara_json(bibliotek)
        elif val == "6":
            bibliotek = läs_json()
        elif val == "7":
            print("👋 Avslutar. Tack för idag!")
            break
        else:
            print("❌ Ogiltigt val. Försök igen.")


if __name__ == "__main__":
    starta_program()
