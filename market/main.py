from market_utils import *

def main():
    # Initialisation du catalogue
    catalog = [
        Fruit(generate_random_number_id(), "Pomme", 100, 1.22),
        Fruit(generate_random_number_id(), "Poire", 50, 2.30),
        Fruit(generate_random_number_id(), "Ananas", 30, 2.90),
    ]

    # Affiche la valeur initiale du stock
    print(f"Valeur initiale du stock : {calculate_stock_value(catalog):.2f} €")

    # Ajout d'un fruit
    fraise = Fruit(generate_random_number_id(), "Fraise", 30, 7.00)
    catalog = add_fruit_to_catalog(catalog, fraise)

    # Recherche d'un fruit par son nom
    fruit_found = read_fruit_by_name(catalog, "Fraise")
    print(f"Fruit trouvé : {fruit_found.name if fruit_found else 'Aucun'}")

    # Suppression d'un fruit
    catalog = remove_fruit_from_catalog(catalog, fraise.id)
    print("Fraise supprimée du catalogue.")

    # Mise à jour de la quantité d'un fruit
    catalog = update_available_fruit_quantity(catalog, catalog[0].id, -10)

    # Vente de 5 ananas
    sale_details = sell_fruit(catalog, catalog[2].id, 5)
    if "error" in sale_details:
        print(f"Erreur : {sale_details['error']}")
    else:
        print(
            f"Vente réalisée : {sale_details['quantity_sold']} {sale_details['fruit_name']}(s) pour un total de {sale_details['total_amount']:.2f} €"
        )

    # Affiche la valeur finale du stock
    print(f"Valeur finale du stock : {calculate_stock_value(catalog):.2f} €")

if __name__ == "__main__":
    main()
