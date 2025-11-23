person={
    "namn": "Christer",
    "ålder": 79,
    "stad": "Stockholm",
    "land": "Sverige"
}

print(person)
print(person["namn"])  # Namnet
print(person["ålder"])  # Åldern
print(person["stad"])  # Staden

print(person.keys())  # Alla nycklar

print(person["namn"])  # Namnet
person["ålder"] = 80  # Ändra åldern
print(person["ålder"])  # Ny ålder
person["yrke"] = "lärare"  # Lägg till yrke
print(person)

for nyckel, värde in person.items():
    print(nyckel + ":", värde)