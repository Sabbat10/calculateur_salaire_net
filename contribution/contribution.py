from contribution.data import list_contribution

def display_contribution_list():
    print("📋 Liste des contributions :")
    print("═" * 40)
    for contribution_type, values in list_contribution.items():
        print(f"💼 Type de contribution : {contribution_type.replace('_', ' ').title()}")
        for contribution in values:
            print(f"📊 Taux : {contribution['taux']} %")
            print(f"💰 Montant prélevé : {contribution['montant_prelever']} €")
        print("═" * 40)


def display_total_prelevement():
    total = 0
    for contributions in list_contribution.values():
        for item in contributions:
            total += item["montant_prelever"]
    return total
    

    