def main():
    # Demande à l'utilisateur de saisir la longueur k et la séquence
    k = int(input("Entrez la longueur k : "))
    sequence = input("Entrez la séquence voulue : ")
    motif_recherche = input("Entrez le motif que vous voulez rechercher : ")
    
    # Crée un ensemble d'alphabet pour la séquence
    alphabet = caracteres_diff(sequence)

    # Initialise l'arbre avec les caractères de l'alphabet
    arbre = init_arbre(alphabet)
    
    # Remplit l'arbre avec les motifs de la séquence
    remplissage_abr(sequence, arbre, alphabet, k)
    positions = recherche_motif(motif_recherche, arbre, k)
    if positions:
        print(f"Positions des suffixes correspondant au motif '{motif_recherche}': {positions}")
    else:
        print(f"Le motif '{motif_recherche}' n'a pas été trouvé dans la séquence.")
    
    
    for pos in positions:
        verif(pos, sequence, motif_recherche)


# Fonction qui retourne l'ensemble des caractères uniques dans une séquence
def caracteres_diff(seq):
    return set(seq)

# Initialise un arbre vide avec les caractères de l'alphabet
def init_arbre(alphabet):
    A = {}
    # Crée un dictionnaire pour chaque caractère de l'alphabet
    for l in alphabet:
        A[l] = {}
    return A

def remplissage_abr(sequence, arbre, alphabet, k):
    suffixes = [""]
    
    # Parcourt la séquence
    for i in range(len(sequence)):
        suff= [""]
        # Ajoute chaque caractère de la séquence à chaque suffixe existant
        for j in range(len(suffixes)):
            if len(suffixes[j])< k:
                suff.append(suffixes[j] + sequence[i])
            # Ne pas insérer le motif si sa longueur dépasse k
        suffixes = suff
        for m in suffixes:    
            inserer_motif_arbre(m, arbre, i - len(m) + 1)
        # Ajoute un nouveau suffixe vide à la liste de suffixes
        suffixes = suff
    
    return arbre

# Insère un motif dans l'arbre avec sa position de départ
def inserer_motif_arbre(motif, arbre, position):
    noeud = arbre
    # Parcourt chaque caractère du motif
    for char in motif:
        # Crée un nouveau nœud si le caractère n'existe pas dans le nœud actuel
        if char not in noeud:
            noeud[char] = {}
        noeud = noeud[char]
    # Initialise la liste des positions si elle n'existe pas
    if "clé" not in noeud:
        noeud["clé"] = []
    # Ajoute la position de départ du motif
    noeud["clé"].append(position)
    
def recherche_motif(motif, arbre, k):
    noeud = arbre
    # Parcourt chaque caractère du motif jusqu'au k-ème caractère
    for char in motif[:k]:
        if char not in noeud:
            # Si le caractère n'existe pas dans l'arbre, le motif n'est pas présent
            return []
        noeud = noeud[char]
    # Si le motif est présent, retourne les positions des suffixes correspondants
    return noeud.get("clé", [])


def verif(pos, sequence, motif):
    motif_len = len(motif)
    # Vérifie si la séquence après la position correspond au motif
    if sequence[pos:pos + motif_len] == motif:
        print(f"La séquence à la position {pos} correspond au motif '{motif}'.")
    else:
        print(f"La séquence à la position {pos} ne correspond pas au motif '{motif}'.") 

main()