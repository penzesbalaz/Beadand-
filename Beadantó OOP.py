from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Egyágyas szoba ára

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Kétágyas szoba ára

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def ar_kiszamolasa(self):
        return self.szoba.ar

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        # Ellenőrizzük, hogy a foglalás dátuma jövőbeli-e
        if datum < datetime.now():
            print("Hiba: A foglalás dátuma nem lehet a múltban!")
            return

        # Ellenőrizzük, hogy a szoba elérhető-e az adott dátumon
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                print("Hiba: A szoba már foglalt ezen a napon!")
                return

        # Ha minden ellenőrzés sikeres, hozzáadjuk a foglalást
        self.foglalasok.append(Foglalas(szoba, datum))
        print("Foglalás sikeres!")

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("Lemondás sikeres!")
        else:
            print("Hiba: A foglalás nem létezik!")

    def foglalasok_listazasa(self):
        print("Foglalások:")
        for i, foglalas in enumerate(self.foglalasok, start=1):
            print(f"{i}. Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# Példa adatokkal feltöltjük a rendszert
szalloda = Szalloda("Példa Szálloda")
szalloda.uj_szoba(EgyagyasSzoba("101"))
szalloda.uj_szoba(KetagyasSzoba("201"))
szalloda.uj_szoba(KetagyasSzoba("202"))

foglalas_kezelo = FoglalasKezelo()
foglalas_kezelo.foglalas(szalloda.szobak[0], datetime.now() + timedelta(days=1))
foglalas_kezelo.foglalas(szalloda.szobak[1], datetime.now() + timedelta(days=2))
foglalas_kezelo.foglalas(szalloda.szobak[2], datetime.now() + timedelta(days=3))

# Felhasználói interfész
while True:
    print("\nVálassz egy műveletet:")
    print("3. Foglalás")
    print("1. Lemondás")
    print("4. Foglalások listázása")
    print("2. Kilépés")
    valasztas = input("Választás: ")

    if valasztas == "1":
        szobaszam = input("Add meg a foglalandó szoba számát: ")
        datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        foglalas_kezelo.foglalas(szalloda.szobak[int(szobaszam) - 1], datum)
    elif valasztas == "2":
        foglalas_szam = input("Add meg a törlendő foglalás sorszámát: ")
        if foglalas_szam.isdigit() and 1 <= int(foglalas_szam) <= len(foglalas_kezelo.foglalasok):
            foglalas_kezelo.lemondas(foglalas_kezelo.foglalasok[int(foglalas_szam) - 1])
        else:
            print("Hibás sorszám!")
    elif valasztas == "3":
        foglalas_kezelo.foglalasok_listazasa()
    elif valasztas == "4":
        break
    else:
        print("Hibás választás!")
