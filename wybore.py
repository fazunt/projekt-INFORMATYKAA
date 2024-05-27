from bronie import Dagger, Shovel, Bow, Club, Rapier
import random

class Gracz:
    def __init__(self):
        self.atak = 23  
        self.zdrowie = 100 
        self.bron = None

    def wybierz_bron(self):
        print("Witaj w grze! Wybierz swoją broń:")
        print("1. Sztylet")
        print("2. Łopata")

        print("3. Łuk")
        print("4. Pałka")
        print("5. Rapier")

        wybor = input("Podaj numer broni: ")

        if wybor == "1":
            self.bron = Dagger()
        elif wybor == "2":
            self.bron = Shovel()

        elif wybor == "3":
            self.bron = Bow()
        elif wybor == "4":
            self.bron = Club()

        elif wybor == "5":
            self.bron = Rapier()
        else:
            print("Nieprawidłowy wybór. Wybierz ponownie.")
            self.wybierz_bron()

    def atakuj(self, przeciwnik):
        print(f"Gracz atakuje przeciwnika używając {self.bron.name}.")
        obrazenia = self.atak + self.bron.attack()

        przeciwnik.odbierz_obrazenia(obrazenia)

    def odbierz_obrazenia(self, obrazenia):
        self.zdrowie -= obrazenia
        if self.zdrowie <= 0:
            print("Przegrałeś! Koniec gry.")
        else:
            print(f"Zostało ci {self.zdrowie} punktów zdrowia.")

class Przeciwnik:
    def __init__(self, nazwa, zdrowie, atak_min, atak_max):

        self.nazwa = nazwa
        self.zdrowie = zdrowie

        self.atak_min = atak_min

        self.atak_max = atak_max


    def atakuj(self):
        obrazenia = random.randint(self.atak_min, self.atak_max)
        return obrazenia

    def odbierz_obrazenia(self, obrazenia):
        self.zdrowie -= obrazenia
        if self.zdrowie <= 0:
            print(f"{self.nazwa} został pokonany!")
        else:
            print(f"{self.nazwa} otrzymuje {obrazenia} obrażeń. Zdrowie: {self.zdrowie}")

def wstep():

    print("Witaj w grze! Twoim zadaniem jest pokonanie przeciwnika za pomocą wybranej broni.")

    print("Każda broń ma swoje unikatowe cechy, wybierz mądrze!")


def wybore():
    wstep()
    gracz = Gracz()
    przeciwnik = Przeciwnik("Potwór", 50, 10, 15)  
    gracz.wybierz_bron()  
    while przeciwnik.zdrowie > 0 and gracz.zdrowie > 0:
        obrazenia_od_przeciwnika = przeciwnik.atakuj()  
        gracz.odbierz_obrazenia(obrazenia_od_przeciwnika)  

        if gracz.zdrowie > 0:
            gracz.atakuj(przeciwnik)  # Gracz atakuje potwora
        else:
            break

if __name__ == "__main__":
    wybore()
