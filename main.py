from employer.employer import get_employee_info
from contribution.contribution import display_contribution_list, display_total_prelevement
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

print("👋 Bienvenue dans le Calculateur de Salaire Net ! 💼")

# Afficher la liste des contributions
# display_contribution_list()

while True:
    print("\n" + "=" * 40)
    print("📋 Sélectionnez une option :")
    print("1️⃣  Enregistrer un nouvel employé 👨‍💼")
    print("2️⃣  Générer un rapport de salaire 📊")
    print("3️⃣ Quitter ❌")

    choice = input("👉 Votre choix : ").strip()
    
    # Enregistrer un nouvel employé
    if choice == "1":
        employee_info = get_employee_info()
        print(f"📄 Informations de l'employé : {employee_info}")
        
        # afficher que le salaire
        print(f"💰 Salaire brut mensuel : {employee_info[3]} €")
        print(f"💸 Salaire de contribution : {display_total_prelevement()} €")

        display_total_prelevement()
        salaire_net = employee_info[3] - display_total_prelevement()
        print(f"💰 Salaire net mensuel : {salaire_net} €")
        
    # Générer un rapport de salaire
    elif choice == "2":
        print("📄 Générer un rapport de salaire")
        employee_info = get_employee_info()

        # Création du PDF
        c = canvas.Canvas("rapport_salaire.pdf", pagesize=A4)
        width, height = A4
        y = height - 50  # Position de départ verticale

        # Entête
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(width / 2, y, "📄 Rapport de Salaire")
        y -= 40

        # Corps du rapport
        c.setFont("Helvetica", 12)
        c.drawString(100, y, f"👤 Nom : {employee_info[0]}")
        y -= 20
        c.drawString(100, y, f"🧒 Prénom : {employee_info[1]}")
        y -= 20
        c.drawString(100, y, f"💼 Poste : {employee_info[2]}")
        y -= 20
        c.drawString(100, y, f"💰 Salaire brut : {employee_info[3]} EUR")
        y -= 20

        salaire_net = employee_info[3] - display_total_prelevement()
        c.drawString(100, y, f"💸 Salaire net : {salaire_net:.2f} EUR")
        y -= 30

        # Liste des contributions
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y, "📋 Contributions :")
        y -= 20
        c.setFont("Helvetica", 11)
        for contribution in display_contribution_list():
            c.drawString(110, y, f"- {contribution}")
            y -= 15

        # Sauvegarde
        c.save()
        print("✅ Rapport de salaire généré avec succès !")

    
    # Quitter le programmej
    elif choice == "3":
        print("👋 Merci d'avoir utilisé le Calculateur de Salaire Net ! À bientôt !")
        break
    else:
        print("❌ Choix invalide, veuillez réessayer.")