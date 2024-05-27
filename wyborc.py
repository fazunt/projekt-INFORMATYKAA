import random

class Gra:
    def __init__(self, nazwy):
        self.nazwy = nazwy

    def graj(self, ruch_gracza):
        ruch_komputera = random.choice(self.nazwy)
        print(f"Komputer wybrał: {ruch_komputera}")
        if ruch_gracza == ruch_komputera:
            print("Remis!")
        elif (ruch_gracza == "kamień" and ruch_komputera == "nożyce") or \
             (ruch_gracza == "papier" and ruch_komputera == "kamień") or \
             (ruch_gracza == "nożyce" and ruch_komputera == "papier"):
            print("Gratulacje, wygrałeś!")
        else:
            print("Niestety, przegrałeś.")

class RozszerzonaGra(Gra):
    def __init__(self):
        super().__init__(("kamień", "papier", "nożyce", "żaba", "wąż", "ptak", "pies", "kot"))

def wyborc():
    print("Witaj w grze Kamień, Papier, Nożyce, Rozszerzona!")
    print("Możliwe ruchy: kamień, papier, nożyce, żaba, wąż, ptak, pies, kot")
    
    rozszerzona_gra = RozszerzonaGra()
    
    while True:
        ruch_gracza = input("Twój ruch: ").lower()
        if ruch_gracza in rozszerzona_gra.nazwy:
            rozszerzona_gra.graj(ruch_gracza)
        else:
            print("Niepoprawny ruch, spróbuj ponownie.")

if __name__ == "__main__":
    wyborc()
