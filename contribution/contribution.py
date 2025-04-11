from contribution.data import list_contribution
import os

# Fonction pour afficher la liste des contributions
def display_contribution_list():
    print(" Liste des contributions :")
    print("═" * 40)
    contribution_lines = []

    for contribution_type, values in list_contribution.items():
        title = f" Type de contribution : {contribution_type.replace('_', ' ').title()}"
        print(title)
        contribution_lines.append(title)

        for contribution in values:
            taux_line = f" Taux : {contribution['taux']} %"
            montant_line = f" Montant prélevé : {contribution['montant_prelever']} EUR"
            print(taux_line)
            print(montant_line)

            contribution_lines.append(taux_line)
            contribution_lines.append(montant_line)

        print("═" * 40)
        contribution_lines.append("═" * 40)

    return contribution_lines


# Fonction pour afficher le total des prélèvements
def display_total_prelevement():
    total = 0
    for contributions in list_contribution.values():
        for item in contributions:
            total += item["montant_prelever"]
    return total
    

    