from employer.employer import get_employee_info
from contribution.contribution import display_contribution_list, display_total_prelevement

print("👋 Bienvenue dans le Calculateur de Salaire Net ! 💼")

# Afficher la liste des contributions
# display_contribution_list()

while True:
    print("\n" + "=" * 40)
    print("📋 Sélectionnez une option :")
    print("1️⃣  Enregistrer un nouvel employé 👨‍💼")
    # print("3️⃣  Afficher la liste des employés 📑")
    print("2️⃣ Quitter ❌")

    choice = input("👉 Votre choix : ").strip()
    if choice == "1":
        employee_info = get_employee_info()
        print(f"📄 Informations de l'employé : {employee_info}")
        
        # afficher que le salaire
        print(f"💰 Salaire brut mensuel : {employee_info[3]} €")
        print(f"💸 Salaire de contribution : {display_total_prelevement()} €")

        display_total_prelevement()
        salaire_net = employee_info[3] - display_total_prelevement()
        print(f"💰 Salaire net mensuel : {salaire_net} €")
        
    elif choice == "2":
        print("👋 Merci d'avoir utilisé le Calculateur de Salaire Net ! À bientôt !")
        break
    else:
        print("❌ Choix invalide, veuillez réessayer.")