class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return (f'Witaj {self.imie} {self.nazwisko}.  Masz{self.wiek} lat.')

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie

    def zmien_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek