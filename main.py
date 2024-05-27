from wstep import wstep1
from wybora import wybora
from wyborb import wyborb
from wyborc import wyborc
from wybord import wybord
from wybore import wybore

def start():
    while True:
        print("Wybierz dalszą opcję swojej przygody:")
        print("a. Gra fabularna")
        print("b. Blackjack - gra karciana")
        print("c. Papier, kamień, nożyce - ze zwierzętami.")
        print("d. Sprawdź swoje szczęście! - zgadywanie liczb.")
        print("e. Pokonaj potwora!!")
        wybor_gry = input("Wybierz literę od a do e (lub q, aby wyjść): ").lower()

        if wybor_gry == 'a':
            wybora()
        elif wybor_gry == 'b':
            wyborb()
        elif wybor_gry == 'c':
            wyborc()
        elif wybor_gry == 'd':
            wybord()
        elif wybor_gry == 'e':
            wybore()
        elif wybor_gry == 'q':
            print("Dziękujemy za grę. Do widzenia!")
            break
        else:
            print("Niepoprawny wybór. Wybierz literę od a do e (lub q, aby wyjść).")

if __name__ == "__main__":
    wstep1()
    start()
