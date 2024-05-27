from random import randint, choice

def wybora():
    print(f'Jesteś w Gdańsku.\n')
    
    print(f'Gdy wychodzisz z samochodu, widzisz grupę osób.')

    print(f'Postanawiasz do nich podejść.')

    print(f'Masz jakiś problem?" - mówi nieznajomy, patrząc na Ciebie.')

    odpowiedz = input(f"Możesz odpowiedzieć, co chcesz: ")

    if odpowiedz:
        print(f'Nieoczekiwanie nieznajomy postanawia zaatakować cie.')
    else:
        print(f'Nieoczekiwanie nieznajomy postanawia zaatakować cie.')


    zlotowki = 4
    life = 20  

    przeciwnicy = [
        ["Napastnik1", 100, 5, 0],  
        ["Napastnik2", 100, 5, 0],
        ["Napastnik3", 120, 6, 0],  
        ["Napastnik4", 120, 6, 0],
        ["Napastnik5", 140, 7, 0],
        ["Napastnik6", 140, 7, 0],
        ["Napastnik7", 160, 8, 0],
        ["Napastnik8", 160, 8, 0]
    ]

    def atak_piescia():
        return randint(3, 6)  

    def atak_sztyletem():
        return randint(5, 10) 

    def wybierz_atak():
        print(f'Wybierz akcję:')
        print(f'A - z pięści')
        print(f'B - ze sztyletu')
        co = input().upper()
        if co == 'A':
            return atak_piescia()
        elif co == 'B':
            return atak_sztyletem()
        else:
            print(f"Nie wybrano dobrej akcji")
            return 0

    def drilowcy():
        return choice(przeciwnicy)

    liczba_pokonanych_przeciwników = 0

    while life > 0:
        opponent = drilowcy()
        print("-" * 40)

        while opponent[1] > 0 and life > 0:
            print(f"Walczysz teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

            life -= opponent[2]
            if life <= 0:
                print(f"Masz {life} HP i {zlotowki} złotówek")
                print(f'Porażka!!! Przegrałeś!!!')
                break

            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_pokonanych_przeciwników += 1

        if liczba_pokonanych_przeciwników % 2 == 0: 
            opponent = drilowcy()
            print(f"Na horyzoncie pojawił się kolejny napastnik!")

    print("-" * 40)
    print(f"KONIEC GRY!")
    print(f"Zabiłeś {liczba_pokonanych_przeciwników} drilowców")

    if liczba_pokonanych_przeciwników == 0:
        print(f'Porażka!!! Przegrałeś!!!')
    elif liczba_pokonanych_przeciwników == 1:
        print(f'Brawo, odtąd żyjesz spokojnym życiem.')
if __name__ == "__main__":
    wybora()