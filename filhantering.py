with open("minfil.txt","w",encoding="utf-8") as fil:

    fil.write("Hej världen!\n")
    fil.write("Detta är min första fil i Python\n")
    fil.write("åäöÅÄÖ\n")


with open("minfil.txt","r",encoding="utf-8") as fil:
    innehall = fil.read()
    print(innehall)