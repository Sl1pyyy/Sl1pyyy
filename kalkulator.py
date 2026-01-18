#This is a calculator space

from chemlib import Compound
from chemlib.chemistry import Solution

def menu():
    print("\nCo chcesz zrobić z tym związkiem?")
    print("1 - Obliczyć masę molową")
    print("2 - Obliczyć procent masowy pierwiastków")
    print("3 - Przygotować roztwór")
    print("4 - Sprawdzić możliwe reakcje")
    print("5 - Stechiometria (gramy → mole)")
    print("0 - Zakończyć program")

def main():
  
    while True:
        wzor = input("Podaj wzór związku chemicznego: ")
        try:
            zwiazek = Compound(wzor)
            break
        except Exception:
            print("Niepoprawny wzór chemiczny! Podaj poprawny wzór.")

    while True:
        menu()
        wybor = input("Wybierz opcję (0-5): ")

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
                roztwor = Solution(zwiazek, c, v)
                print(f"Potrzebna masa substancji: {roztwor.mass:.2f} g")
            except:
                print("Błędne dane!")

        elif wybor == "4":
            print("Reakcje chemiczne:")
            try:
                if zwiazek.reactions:
                    for r in zwiazek.reactions:
                        print(r)
                else:
                    print("Brak zapisanych reakcji.")
            except:
                print("Nie można pobrać reakcji.")

        elif wybor == "5":
            try:
                g = float(input("Podaj masę w gramach: "))
                mole = g / zwiazek.molar_mass()
                print(f"{g:.2f} g = {mole:.4f} mola")
            except:
                print("Błędna wartość!")

        elif wybor == "0":
            print("Do zobaczenia 👋")
            break

        else:
            print("Nieprawidłowy wybór!")

        if input("\nCzy chcesz coś jeszcze zrobić? (tak/nie): ").lower() != "tak":
            print("Program zakończony.")
            break

if __name__ == "__main__":
    main()








