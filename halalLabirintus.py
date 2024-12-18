kredit = 10
bolygo = "Thorodin"
tank = 0
aru = 0
max_aru = 5
valFel = []
bolygok = ["Ydalir", "Vidar", "Folkvang"]
felszerelesek = ["dokkoló egység", "tolmácsgép", "konténer"]
valaszthatoAru = ["üzemanyag", "felszerelés","áru"]
print(f"Üdvözlünk a {bolygo} bolygón! \n\t")
termek = input("Mit szeretnél vásárolni?:")
while not termek in valaszthatoAru:
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
                if 0 < kredit - 10:
                    kredit -= 10
                    valFel.append(valasztott)
                else:
                    print("Nincs rá pénzed!")
            if valasztott == "tolmácsgép":
                if 0 < kredit - 5:
                    kredit -= 5
                    valFel.append(valasztott)
                else:
                    print("Nincs rá pénzed!")
        if valasztott in valFel and valasztott != "konténer":
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
        tank + menny == tank
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
    if bolygo == "Thorodin":
        if 0.4 < tank:
            bolygo == "Ydalir"
        else:
            print("Üres a tank bolond, előbb tankoljál.")
    if bolygo == "Vidar":
        if 0.4 < tank:
            bolygo == "Ydalir"




