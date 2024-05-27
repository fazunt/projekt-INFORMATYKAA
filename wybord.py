import random

class Gra:
    def __init__(self, zakres):

        self.zakres = zakres

        self.liczba = random.randint(1, zakres)
        self.wygrana = False

    def sprawdz(self, zgadniete):
        if zgadniete == self.liczba:

            print("Brawo! Zgadłeś liczbę!")
            self.wygrana = True

        elif zgadniete < self.liczba:

            print("Liczba jest większa.")
        else:

            print("Liczba jest mniejsza.")

class Interfejs:
    def __init__(self, zakres):
        self.gra = Gra(zakres)

    def rozpocznij_gre(self):
        print(f"Wylosowano liczbę z zakresu od 1 do {self.gra.zakres}. Zgadnij, jaka to liczba!")

    def zgaduj(self, liczba):
        self.gra.sprawdz(liczba)

        if self.gra.wygrana:
            
            print("Koniec gry!")

def wybord():
    interfejs = Interfejs(100)  

    interfejs.rozpocznij_gre()
    
    for proba in range(5):
        try:
            zgadywana = int(input("Podaj swoją liczbę: "))

            interfejs.zgaduj(zgadywana)

            if interfejs.gra.wygrana:
                break
        except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
    else:
        print("Przekroczono limit prób. Koniec gry!")

if __name__ == "__main__":
    wybord()