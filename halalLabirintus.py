kredit = 10
bolygo = "Thorodin"
tank = 0
aru = 0
max_aru = 5
valFel = []
bolygok = ["Ydalir", "Vidar", "Folkvang"]

print(f"Üdvözlünk a {bolygo} bolygón!\n")
print("Elérhető termékek: üzemanyag, felszerelés, áru")

felszerelesek = ["dokkoló egység", "tolmácsgép", "konténer"]

while True:
    termek = input("Mit szeretnél vásárolni (semmit, ha nem vásárolsz)? ").lower()
    if termek == "semmit":
        break

    if termek == "felszerelés":
        print(f"Elérhető felszerelések: {', '.join(felszerelesek)}")
        valasztott = input("Melyiket választod? ").lower()
        if valasztott in felszerelesek:
            arak = {"dokkoló egység": 10, "tolmácsgép": 5, "konténer": 3}
            if kredit >= arak[valasztott]:
                kredit -= arak[valasztott]
                valFel.append(valasztott)
                felszerelesek.remove(valasztott)
                print(f"Sikeresen megvásároltad a(z) {valasztott}-t.")
            else:
                print("Nincs elég kredited.")
        else:
            print("Ilyen felszerelés nincs.")

    elif termek == "üzemanyag":
        menny = input("Fél vagy tele tank? (fél/tele): ").lower()
        if menny == "fél":
            menny = 0.5
        elif menny == "tele":
            menny = 1.0
        else:
            print("Érvénytelen választás.")
            continue

        if tank + menny > 1.0:
            print("Már tele van a tankod!")
        elif kredit >= menny * 2:
            tank += menny
            kredit -= menny * 2
            print("Üzemanyag vásárlása sikeres.")
        else:
            print("Nincs elég kredited.")

    elif termek == "áru":
        try:
            aruMenny = int(input("Mennyi árut szeretnél vásárolni? "))
            if aru + aruMenny <= max_aru:
                aru += aruMenny
                print(f"Sikeresen vásároltál {aruMenny} egység árut.")
            else:
                print("Nem fér el nálad ennyi áru.")
        except ValueError:
            print("Kérlek számot adj meg!")

    else:
        print("Ilyen kategória nincs!")

print("\nElérhető bolygók: Ydalir, Vidar, Folkvang")
utazas = input("Hová szeretnél utazni? ").capitalize()

if utazas in bolygok:
    if bolygo == "Thorodin" and utazas == "Ydalir" and tank >= 0.4:
        bolygo = utazas
        print(f"Sikeresen megérkeztél {bolygo}-ra.")
    else:
        print("Nem tudsz oda utazni.")
else:
    print("Ilyen bolygó nincs.")
