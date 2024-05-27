from osoba import Osoba
import zmienne

def wstep1():

    zacznij_gre = input(f'Jesli chcesz przystąpić do gry naciśnij --> Tak\n'
                        f'Jesli chcesz zakończyć grę naciśnij --> Nie\n')

    if zacznij_gre == 'Tak':
            imie, nazwisko, wiek = zmienne.pobierz_dane()
            osoba = Osoba(imie, nazwisko, wiek)
            print(osoba.przedstaw_sie())
        
    elif zacznij_gre == 'Nie':
        print(f'Gra zostaje przerwana.')
        return None