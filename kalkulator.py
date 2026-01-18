#This is a calculator space

from chemlib import Compound, Reaction
from chemlib.chemistry import Solution


def menu():
    print("\nCo chcesz zrobić z tym związkiem?")
    print("1 - Obliczyć masę molową")
    print("2 - Obliczyć procent masowy pierwiastków")
    print("3 - Przygotować roztwór")
    print("4 - Stechiometria (gramy → mole)")
    print("0 - Zakończyć program")

def main():

    while True:
        wzor = input("Podaj wzór związku chemicznego: ")
        try:
            zwiazek = Compound(wzor)
            break
        except Exception:
            print("Niepoprawny wzór chemiczny! Podaj poprawny wzór.")

    menu()
    while True:
        wybor = input("Wybierz opcję (0-4) lub 'm' aby pokazać menu: ")

        if wybor.lower() == 'm':
            menu()
            continue

        if wybor == "1":
            print(f"Masa molowa {wzor}: {zwiazek.molar_mass():.2f} g/mol")

        elif wybor == "2":
            print("Procent masowy pierwiastków:")
        

            for pierwiastek in zwiazek.occurences:
                    procent = zwiazek.percentage_by_mass(pierwiastek)
                    print(f"{pierwiastek}: {procent:.2f} %")


        elif wybor == "3":
            try:
                c = float(input("Podaj stężenie molowe (mol/dm³): "))
                v = float(input("Podaj objętość roztworu (dm³): "))

                n = c * v
                print(f"Liczba moli  {wzor} w tej objętości: {n:.4f} mol")
                print(f'Masa {wzor}: {n * zwiazek.molar_mass():.2f} g')

            except ValueError:
                print("Błąd! Podaj poprawne liczby.")
            

        elif wybor == "4":
            try:
                g = float(input("Podaj masę w gramach: "))
                mole = g / zwiazek.molar_mass()
                print(f"{g:.2f} g = {mole:.4f} mola")
            except:
                print("Błędna wartość!")

        elif wybor == "0":
            print("Elo")
            break

        else:
            print("Nieprawidłowy wybór!")
            menu()


if __name__ == "__main__":
    main()








