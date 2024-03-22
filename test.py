def main():
    # Demande à l'utilisateur de saisir la longueur k et la séquence
    k = int(input("Entrez la longueur k : "))
    sequence = input("Entrez la séquence voulue : ")
    
    # Crée un ensemble d'alphabet pour la séquence
    alphabet = caracteres_diff(sequence)

    # Initialise l'arbre avec les caractères de l'alphabet
    arbre = init_arbre(alphabet)
    
    # Remplit l'arbre avec les motifs de la séquence
    remplissage_abr(sequence, arbre, alphabet, k)
    
    
    
    afficher_arbre(arbre)

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

# Remplit l'arbre avec les motifs de la séquence
def remplissage_abr(sequence, arbre, alphabet, k):
    # Parcourt la séquence
    for i in range(len(sequence)):
        # Génère tous les suffixes de la séquence à partir de l'index actuel
        for j in range(i + 1, min(i + k + 1, len(sequence)) + 1):
            suffixe = sequence[i:j]
            # Vérifie si le suffixe est inférieur ou égal à la longueur k
            if len(suffixe) <= k:
                inserer_motif_arbre(suffixe, arbre, i)  # Insère le suffixe dans l'arbre
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

            
def afficher_arbre(arbre, niveau=0):
    for cle, valeur in arbre.items():
        if cle != "clé":
            print(" " * niveau * 2, cle, ":", valeur["clé"])
            afficher_arbre(valeur, niveau + 1)
            

main()
