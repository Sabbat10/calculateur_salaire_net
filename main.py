from employer.employer import get_employee_info, display_employee_list

print("👋 Bienvenue dans le Calculateur de Salaire Net ! 💼")

while True:
    print("\n" + "=" * 40)
    print("📋 Sélectionnez une option :")
    print("1️⃣  Enregistrer un nouvel employé 👨‍💼")
    print("2️⃣  Afficher la liste des employés 📑")
    print("3️⃣  Quitter ❌")

    choice = input("👉 Votre choix : ").strip()
    if choice == "1":
        employee_info = get_employee_info()
        print(f"📄 Informations de l'employé : {employee_info}")

        
    # Enregistrer l'employé dans la liste
    elif choice == "2":
        print("👤 Voici le profil de l'employé :")
        display_employee_list()
        
    # break
    elif choice == "3":
        print("👋 Merci d'avoir utilisé le Calculateur de Salaire Net ! À bientôt !")
        break
    else:
        print("❌ Choix invalide, veuillez réessayer.")