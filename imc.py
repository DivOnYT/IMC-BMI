from colorama import Fore, init
init()
def imc(taille, poids):
    print("Calculer L'IMC (Indice de Masse Corporelle) \n")
    print("Tool créée par Div_YT")
    try:
        imc = float(poids) / (float(taille) * float(taille))
        if imc < 18.5:
            print(f"Votre IMC est de {imc}, vous êtes en {Fore.BLUE}SOUS-POIDS{Fore.RESET}.")
        elif imc > 18.5 and imc < 25:
            print(f"Votre IMC est de {imc}, vous êtes {Fore.GREEN}NORMAL{Fore.RESET}.")
        elif imc > 25 and imc < 30:
            print(f"Votre IMC est de {imc}, vous êtes en {Fore.ORANGE}SURPOIDS{Fore.RESET}. Faites des activités sportives régulières .")
        elif imc > 30 and imc < 35:
            print(f"Votre IMC est de {imc}, vous êtes en état d'{Fore.RED}OBESITE{Fore.RESET}. Faites du sport.")
        elif imc > 35:
            print(f"Votre IMC est de {imc}, vous êtes en état d'{Fore.RED}OBESITE SEVERE{Fore.RESET}. Faites un regime et du sport.")
        return imc
    except:
        print("Vérifiez les valeurs entrées !! Erreur !! ")

def start():
    poids = input(" Votre Poids >>> ")
    if poids:
        taille = input(" Votre Taille (en Mètres) >>> ")
        if taille:
            imc(taille, poids)
            print("Fin du Programme. Appuyez sur ENTER pour Quitter le programme")
            input()
        else:
            print("Entrez une valeur pour la Taille.")
            taille = input(" Votre Taille (en Mètres ex: 1.85) >>> ")
    else:
        print("Entrez une valeur pour votre Poids.")
        poids = input(" Votre Poids (en KiloGrammes. ex: 52.1) >>> ")

if __name__ == "__main__":
    start()
