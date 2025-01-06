from typing import Any, Dict, List, Optional, Union

# Exercice 1 : Trouver un item par son nom
def find_in_tree(node: Dict[str, Any], target: str) -> Optional[Dict[str, Any]]:
    """
    Trouve un noeud dans l'arbre par son nom.
    """
    if node["name"] == target:
        return node
    if "children" in node:
        for child in node["children"]:
            result = find_in_tree(child, target)
            if result:
                return result
    return None

# Exercice 2 : Majuscules et emojis
def upper_case_and_surround(text: str) -> str:
    """
    Transforme une chaîne en majuscules et l'entoure avec des emojis  .
    """
    return f" {text.upper()} "

def modify_as_you_go(node: Dict[str, Any], fn: callable) -> Dict[str, Any]:
    """
    Applique une transformation à tous les noeuds de l'arbre.
    """
    node["name"] = fn(node["name"])
    if "children" in node:
        node["children"] = [modify_as_you_go(child, fn) for child in node["children"]]
    return node

# Exercice 3 : Retourner toutes les valeurs
def get_all_values(node: Dict[str, Any], results: Optional[List[str]] = None) -> List[str]:
    """
    Retourne une liste contenant toutes les valeurs des noeuds de l'arbre.
    """
    if results is None:
        results = []
    results.append(node["name"])
    if "children" in node:
        for child in node["children"]:
            get_all_values(child, results)
    return results

# Exercice 4 : Trouver un noeud et son chemin
def find_node_and_path(nodes: List[Dict[str, Any]], target: str, path: Optional[List[str]] = None) -> Optional[List[str]]:
    """
    Retourne le chemin d'un noeud par son nom.
    """
    if path is None:
        path = []
    for node in nodes:
        current_path = path + [node["name"]]
        if node["name"] == target:
            return current_path
        if "children" in node:
            result = find_node_and_path(node["children"], target, current_path)
            if result:
                return result
    return None

# Exercice 5 : Fonction personnalisée - Compter les noeuds
def count_nodes(node: Dict[str, Any]) -> int:
    """
    Compte le nombre total de noeuds dans l'arbre.
    """
    count = 1
    if "children" in node:
        count += sum(count_nodes(child) for child in node["children"])
    return count
