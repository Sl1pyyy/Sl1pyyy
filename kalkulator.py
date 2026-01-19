#This is a calculator space

from chemlib import Compound, Reaction
from chemlib.chemistry import Solution

toksyk = {
    "NaOH": "Silnie żrący (zasada sodowa). Powoduje poważne oparzenia chemiczne i uszkodzenia oczu",
    "KOH": "Silnie żrący (zasada potasowa). Wysoce reaktywny, niszczy tkanki organiczne",
    "HCl": "Kwas solny. Gaz drażniący drogi oddechowe, roztwór silnie żrący. Powoduje korozję metali",
    "H2SO4": "Kwas siarkowy(VI). Silnie higroskopijny i żrący. Powoduje zwęglenie tkanek organicznych",
    "HNO3": "Kwas azotowy(V). Silny utleniacz. Powoduje charakterystyczne żółte zabarwienie skóry (reakcja ksantoproteinowa)",
    "HF": "Kwas fluorowodorowy. EKSTREMALNIE NIEBEZPIECZNY. Przenika przez skórę do kości, wiążąc wapń. Może być śmiertelny nawet przy małych oparzeniach",

    "CO": "Tlenek węgla (czad). Bezwonny, cichy zabójca. Silnie wiąże się z hemoglobiną, blokując transport tlenu",
    "CO2": "Dwutlenek węgla. Gaz duszący w wysokich stężeniach. Powoduje kwasicę oddechową",
    "NH3": "Amoniak. Gaz o duszącym zapachu. Drażni błony śluzowe i oczy. Toksyczny dla organizmów wodnych",
    "Cl2": "Chlor. Gaz bojowy, silnie drażniący płuca. Powoduje obrzęk płuc",
    "H2S": "Siarkowodór. Zapach zgniłych jaj. W wysokich stężeniach poraża nerw węchowy (staje się niewyczuwalny) i blokuje oddychanie komórkowe",

    "CH3OH": "Metanol. Silna trucizna. Spożycie 10 ml powoduje ślepotę, 30 ml – śmierć. Uszkadza nerw wzrokowy",
    "C2H5OH": "Etanol. Substancja psychoaktywna. W dużych dawkach toksyczna dla wątroby i układu nerwowego",
    "C6H6": "Benzen. Silnie rakotwórczy (karcynogen). Powoduje białaczkę. Uszkadza szpik kostne",
    "CHCl3": "Chloroform. Działa toksycznie na wątrobę i nerki. Podejrzewany o działanie rakotwórcze",
    "CH3COCH3": "Aceton. Drażniący, łatwopalny. Działa wysuszająco na skórę",

    "KCN": "Cyjanek potasu. Ekstremalnie toksyczny. Blokuje enzymy oddechowe w mitochondriach. Śmierć następuje w kilka minut",
    "NaCN": "Cyjanek sodu. Działa identycznie jak cyjanek potasu – blokuje oddychanie komórkowe",
    "AgNO3": "Azotan srebra. Żrący, pozostawia na skórze ciemne, trudne do usunięcia plamy srebra metalicznego",
    "CuSO4": "Siarczan miedzi(II). Toksyczny po spożyciu. Silnie szkodliwy dla środowiska wodnego",
    "H2O2": "Nadtlenek wodoru. Silny utleniacz. Stężony (perhydrol) powoduje białe plamy na skórze i bolesne oparzenia",
    "KMnO4": "Nadmanganian potasu. Utleniacz. Plami skórę na brązowo. Działa drażniąco",
    "HgCl2": "Chlorek rtęci(II). Silnie toksyczny, powoduje nieodwracalne uszkodzenia nerek i układu nerwowego",

    "H2O": "Woda. Substancja nietoksyczna. Niezbędna do życia",
    "NaCl": "Chlorek sodu (sól kuchenna). Niska toksyczność. Nadmiar szkodzi nerkom i układowi krwionośnemu",
    "C12H22O11": "Sacharoza (cukier). Nietoksyczna, wysoki indeks glikemiczny",
    "NaHCO3": "Wodorowęglan sodu (soda oczyszczona). Nietoksyczna, stosowana w przemyśle spożywczym"
}

def toks(compound_obj):
    formula = compound_obj.formula
    if formula in toksyk:
        return toksyk[formula]

    occur = compound_obj.occurences
    if "Pb" in occur or 'Hg' in occur or 'Cd' in occur:
        return "Uwaga: Zawiera metale ciężkie. Wykazuje tendencję do bioakumulacji i działania neurotoksycznego"
    if "As" in occur:
        return "Uwaga: Związek arsenu. Silnie toksyczny i rakotwórczy"

    return "Brak szczegółowych danych w lokalnej bazie"


def naglowek(compound):
    print(f"\n Analiza dla wzoru: {compound.formula}")
    print(f" Toksykologia: {toks(compound)}")

def menu():
    print("\nCo chcesz zrobić?")
    print("1 - Obliczyć masę molową")
    print("2 - Obliczyć procent masowy pierwiastków")
    print("3 - Przygotować roztwór")
    print("4 - Bilansowanie reakcji (dodaj drugi reagent)")
    print("5 - Stechiometria (gramy → mole)")
    print("0 - Zakończyć program")


def main():
    while True:
        wzor = input("\nPodaj wzór związku chemicznego (lub 'exit' aby wyjść): ")
        if wzor.lower() == 'exit': break

        try:
            zwiazek = Compound(wzor)
        except Exception:
            print("Niepoprawny wzór chemiczny!")
            continue

        while True:
            menu()
            wybor = input("Wybierz opcję (0-5): ")

            if wybor == "1":
                naglowek(zwiazek)
                print(f"Masa molowa: {zwiazek.molar_mass():.2f} g/mol")

            elif wybor == "2":
                naglowek(zwiazek)
                print("Procent masowy pierwiastków:")
                for pierwiastek, ilosc in zwiazek.occurences.items():
                    procent = zwiazek.percentage_by_mass(pierwiastek)
                    print(f" - {pierwiastek}: {procent:.2f} %")

            elif wybor == "3":
                try:
                    c = float(input("Podaj stężenie molowe (mol/dm³): "))
                    v = float(input("Podaj objętość roztworu (dm³): "))
                    roztwor = Solution(zwiazek, c, v)
                    naglowek(zwiazek)
                    print(f"Potrzebna masa substancji: {roztwor.mass:.2f} g")
                except:
                    print("Błędne dane!")

            elif wybor == "4":
                try:
                    reagent2_str = input(f'Podaj wzór drugiego substratu do reakcji z {zwiazek.formula}: ')
                    reagent2 = Compound(reagent2_str)
                    produkt_str = input('Podaj wzór przewidywanego produktu: ')
                    produkt = Compound(produkt_str)

                    reakcja = Reaction([zwiazek, reagent2], [produkt])
                    reakcja.balance()

                    naglowek(zwiazek)
                    print('Zbilansowane równanie:')
                    print(reakcja.formula)
                except:
                    print('Nie udało się zbilansować takiej reakcji. Sprawdź poprawność chemiczną')

            elif wybor == "5":
                try:
                    g = float(input("Podaj masę w gramach: "))
                    mole = g / zwiazek.molar_mass()
                    naglowek(zwiazek)
                    print(f"Wynik: {g:.2f} g = {mole:.4f} mola")
                except:
                    print("Błędna wartość!")

            elif wybor == "0":
                break
            else:
                print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()







