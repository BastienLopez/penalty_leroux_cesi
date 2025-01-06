from pasta_utils import *

def main():
    # Exemple de structure de l'arbre pastaTree
    pastaTree = {
        "name": "Pasta",
        "children": [
            {"name": "Spaghetti"},
            {"name": "Macaroni"},
            {
                "name": "Autres pâtes",
                "children": [
                    {"name": "Gnocchi"},
                    {"name": "Ravioli"},
                ]
            }
        ]
    }

    # Exercice 1 : Trouver un noeud par son nom
    target = "Gnocchi"
    result = find_in_tree(pastaTree, target)
    print(f"Résultat pour {target} : {result}")

    # Exercice 2 : Modifier l'arbre avec des emojis
    modified_tree = modify_as_you_go(pastaTree, upper_case_and_surround_with_emoji)
    print("Arbre modifié avec des emojis :", modified_tree)

    # Exercice 3 : Obtenir toutes les valeurs de l'arbre
    values = get_all_values(pastaTree)
    print("Toutes les valeurs de l'arbre :", values)

    # Exercice 4 : Trouver un noeud et son chemin
    path = find_node_and_path([pastaTree], "Gnocchi")
    print(f"Chemin pour 'Gnocchi' : {path}")

    # Exercice 5 : Fonctionnalité personnalisée - Compter les noeuds
    node_count = count_nodes(pastaTree)
    print("Nombre total de noeuds :", node_count)

if __name__ == "__main__":
    main()
