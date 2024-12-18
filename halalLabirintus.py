import random
from random import randint

kredit = 10
bolygo = "Thorodin"
tank = 0
aru = 0
max_aru = 5
valFel = []
esely = 70
bolygok = ["Ydalir", "Vidar", "Folkvang", "Thorodin"]
felszerelesek = ["dokkoló egység", "tolmácsgép", "konténer"]
valaszthatoAru = ["üzemanyag", "felszerelés","áru", "semmit"]
jatek = "igen"
while(jatek == "igen"):
    print(f"Üdvözlünk a {bolygo} bolygón! \n\t")
    if "tolmácsgép" not in valFel:
        szazalek = random.randint(-10, 50)
        kredit = kredit + (aru / 100 * szazalek)
        aru -= aru
    if "tolmácsgép" in valFel:
        szazalek = random.randint(5, 65)
        kredit = kredit + (aru / 100 * szazalek)
        aru -= aru

    termek = ""
    while not termek in valaszthatoAru or termek != "semmit":
     termek = input("Mit szeretnél vásárolni?:")



     if termek == "felszerelés":
                print(f"Elérhető felszereléseink:{felszerelesek}")
                valasztott = input("Melyiket választod?:")
                while not(valasztott in felszerelesek):
                    print("Ilyenünk nincs sajnos")
                    valasztott = input("Melyiket választod?:")
                    if valasztott == "konténer":
                        if 0 < kredit - 3:
                            kredit -= 3
                            valFel.append(valasztott)
                        else:
                            print("Nincs rá pénzed!")
                    if valasztott == "dokkoló egység":
                        if 0 < kredit - 1:
                            kredit -= 1
                            valFel.append(valasztott)
                        else:
                            print("Nincs rá pénzed!")
                    if valasztott == "tolmácsgép":
                        if 0 < kredit - 5:
                            kredit -= 5
                            valFel.append(valasztott)
                        else:
                            print("Nincs rá pénzed!")
                if valasztott in valFel and valasztott != "konténer" or "semmit":
                    felszerelesek.remove(valasztott)

                print(valFel)
     if termek == "üzemanyag":
            menny = input("Fél vagy tele tank?:")
            if menny == "fél":
                menny = 0.5
            elif menny == "tele":
                menny = 1
            if 1 < menny + tank:
                print("Már tele van a tankod, nem vásárolhatsz üzemanyagot!")
                tank == tank
            elif kredit - (menny * 2)  < 0:
                print("Nincs rá pénzed, nem vásárolhatsz.")
            else:
                tank == tank + menny
                kredit = kredit - (menny * 2)
     if termek == "áru":
            aruMenny = int(input("Mennyi árut szeretnél vásárolni?:"))
            if max_aru < aruMenny + aru:
                print("Bocsi, ennyi áru nem fér el nálad. Adj meg másik mennyiséget, vagy vásárolj mást!")
                aruMenny = int(input("Mennyi árut szeretnél vásárolni?:"))
            else: aru += aruMenny
    utazas = input("Hová szeretnél utazni?:")
    while not(utazas in bolygok):
        print("Ilyen bolygó nincsen, válassz másikat!")
        utazas = input("Hová szeretnél utazni?:")
    while(bolygo == "Folkvang" and utazas != "Vidar"):
            print("Ide nem mehetsz bolond, túl messze van. Válassz másikat!")
            utazas = input("Hová szeretnél utazni?:")
    if utazas == "Ydalir":
        if bolygo == "Thorodin" and 0.4 < tank:
            print("Utazás megkezdése.")
        elif bolygo == "Thorodin" and 0.4 < tank:
            print("Utazás megkezdése.")
        else:
                print("Üres a tank bolond, előbb tankoljál.")
    if utazas == "Thorodin":
        if bolygo =="Vidar" and 0.9 < tank:
            print("Utazás megkezdése.")
        elif bolygo == "Ydalir" and 0.4 < tank:
            print("Utazás megkezdése")
        else:
            print("Üres a tank bolond, előbb tankoljál.")
    hova = utazas

    if "dokkoló egység" in valFel:
        bolygo == hova
    else:
        leszallas = random.randint( 1, 100)
        if esely < leszallas:
            print("Sajnos nem tudtál leszállni.")
        else:
            bolygo == hova
            print(f"Sikeresen átutaztál a {bolygo} bolygóra ")
    jatek = input("Folytassuk a játékot?")


