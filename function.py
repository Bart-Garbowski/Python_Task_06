def main_separator():
    print("#" * 81)
    print(f"{'#' * 34} \33[36m MAIN MENU \33[39m {'#' * 34}")
    print("#" * 81)


class Uczen:

    def __init__(self):
        self.name = None
        self.klasa = None

    def details(self):
        name = input("Podaj imie ucznia: ")
        class_name = input("Podaj klase: ")
        self.name = name
        self.class_name = class_name


class Wychowawca:

    def __init__(self):
        self.name = None
        self.class_name = None
        self.subject = None

    def details(self):
        name = input("Podaj imie wychowawcy: ")
        class_names = []
        while True:
            class_name = input("Podaj klase: ").strip()
            if not class_name:
                break
            else:
                class_names.append(class_name)
        self.name = name
        self.class_name = class_names


class Nauczyciel:

    def __init__(self):
        self.name = None
        self.class_name = None
        self.subject = None

    def details(self):
        name = input("Podaj imie nauczyciela: ")
        subject = input("Przedmiot: ")
        class_names = []
        while True:
            class_name = input("Podaj klase: ").strip()
            if not class_name:
                break
            else:
                class_names.append(class_name)
        self.name = name
        self.class_name = class_names
        self.subject = subject