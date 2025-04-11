# from employer.data import information_employer

print("Entrez les informations suivantes :")

# Fonction pour obtenir les informations d'un employé
def get_employee_info():
    print(" Enregistrement d’un nouvel employé")
    print("==" * 20)

    # 🔹 Nom
    name = input(" Nom de l'employé : ").strip()

    # 🔹 Âge (avec validation)
    while True:
        try:
            age = int(input(" Âge de l'employé : "))
            if age <= 0:
                print(" L'âge doit être supérieur à 0.")
            else:
                break
        except ValueError:
            print(" Âge invalide, veuillez entrer un nombre entier.")

    # 🔹 Poste
    position = input(" Poste de l'employé : ").strip()

    # 🔹 Salaire (avec validation)
    while True:
        try:
            salary = float(input(" Salaire brut mensuel (en euros) : "))
            if salary <= 0:
                print(" Le salaire doit être supérieur à 0.")
            else:
                break
        except ValueError:
            print(" Salaire invalide, veuillez entrer un montant valide.")

    print(" Employé enregistré avec succès !\n")
    return name, age, position, salary


# Fonction pour ajouter un employé à la liste
# def add_employee_to_list(employee_info):
#     name, age, position, salary = employee_info
#     new_employee = {
#         "name": name,
#         "age": age,
#         "position": position,
#         "salary": salary
#     }
#     information_employer.append(new_employee)
#     print(f"✅ Employé {name} ajouté à la liste !")
    

# # Fonction pour afficher la liste des employés
# def display_employee_list():
#     print("📋 Liste des employés :")
#     print("═" * 40)
#     for employee in information_employer:
#         print(f"👤 Nom      : {employee['name']}")
#         print(f"🎂 Âge      : {employee['age']} ans")
#         print(f"💼 Poste    : {employee['position']}")
#         print(f"💰 Salaire  : {employee['salary']} €")
#         print("—" * 40)
#     print("═" * 40)
