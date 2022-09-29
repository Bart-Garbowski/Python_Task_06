from function import main_separator
from function import Uczen
from function import Wychowawca
from function import Nauczyciel
main_menu = ("utworz", "zarzadzaj", "zakoncz")
ALLOWED_COMMANDS_utworz = ("uczen", "nauczyciel", "wychowawca", "koniec")
ALLOWED_COMMANDS_zarzadzaj = ("klasa", "uczen", "nauczyciel", "wychowawca", "koniec")


uczen_lista = []
nauczyciel_lista = []
wychowawca_lista = []

while True:
    main_separator()
    print(f"Dozwolone trzy komendy: ---{main_menu}--- \n"
          f"--utworz--       utworzy nowy profil uzytkownika\n"
          f"--zarzadzaj--    pokaze dane dotyczace ucznia, klasy etc.\n"
          f"--zakoncz--      konczy dzialanie programu")
    command = input("Prosze wpisac komende: ")
    command = command.lower()

    if command == "zakoncz":
        break

    if command == "utworz":
        while True:
            print("_" * 81)
            print(f"Dozwolne typy uzytkownikow: {ALLOWED_COMMANDS_utworz}")
            command = input("Wpisz typ uzytkownika lub wroc do glownego menu wpisujac --koniec--: ")
            command = command.lower()

            if command not in ALLOWED_COMMANDS_utworz:
                print("Niepoprawny typ uzytkownika!")
                continue

            elif command == "koniec":
                break

            elif command == "uczen":
                obj = Uczen()
                uczen_lista.append(obj)

            elif command == "nauczyciel":
                obj = Nauczyciel()
                nauczyciel_lista.append(obj)

            elif command == "wychowawca":
                obj = Wychowawca()
                wychowawca_lista.append(obj)

            obj.details()

    if command == "zarzadzaj":
        while True:
            print("_" * 81)
            print(f"Dozwolne typy uzytkownikow: {ALLOWED_COMMANDS_zarzadzaj}")
            command = input("Wpisz typ uzytkownika lub wroc do glownego menu wpisujac --koniec--: ")
            command = command.lower()

            if command not in ALLOWED_COMMANDS_zarzadzaj:
                print("Niepoprawny typ uzytkownika!")
                continue

            elif command == "koniec":
                break

            elif command == "uczen":
                ucz_name = input("Podaj imie ucznia: ")
                for uczen in uczen_lista:
                    if ucz_name == uczen.name:
                        for nauczyciel in nauczyciel_lista:
                            if uczen.class_name in nauczyciel.class_name:
                                print(nauczyciel.name)

            elif command == "klasa":
                klasa = input("Podaj klase: ")
                for uczen in uczen_lista:
                    if klasa == uczen.class_name:
                        print(f"Imie ucznia: {uczen.name}")
                        print(f"Imie wychowawcy: {[wychowawca.name for wychowawca in wychowawca_lista]}")

            elif command == "nauczyciel":
                na_name = input("Podaj imie nauczyciela: ")
                for nauczyciel in nauczyciel_lista:
                    if na_name == nauczyciel.name:
                        for uczen in uczen_lista:
                            if uczen.class_name in nauczyciel.class_name:
                                print(uczen.name)

            elif command == "wychowawca":
                wych_name = input("Podaj imie wychowawcy: ")
                for wychowawca in wychowawca_lista:
                    if wych_name == wychowawca.name:
                        for uczen in uczen_lista:
                            if uczen.class_name in wychowawca.class_name:
                                print(uczen.name)
