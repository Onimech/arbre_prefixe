

def main ():
     3
     k = int(input("Entrez la longueur k : "))
     sequence = input("Entrez la séquence voulue :")
     alphabet = caracteres_diff(sequence)
     print(sequence)
     print(alphabet)

     degre = len(alphabet)
     print(degre)
     arbre = construire_arbre(degre, k)
     print(arbre)
def caracteres_diff(seq):
     return(set(seq))

#for i in nbalphabet
#new fils"i"

#noeud des arbre : liste contenant le dernier caractere du motif et les positions du motif


#registe des derniers motifs rencontrés, ajout du caractère rencontré aux motifs
#elimination des motifs de longueur supérieure à k
def construire_arbre(degre, niveau, profondeur=1, nom_noeud='racine'):
    if niveau == 0: #si on donne k = 0
        return None
    else:
        sous_arbres = {}
        for i in range(1, degre + 1):
            nom_enfant = f"prof{profondeur}_enfant_{i}"
            sous_arbres[nom_enfant] = construire_arbre(degre, niveau-1, profondeur + 1, nom_enfant)

        return {
            'nom_noeud': nom_noeud,
            'sous_arbres': sous_arbres
        }

def afficher_arbre(arbre, niveau=1):
    if arbre is not None:
        indent = '  ' * niveau
        print(f"{indent}{arbre['nom_noeud']}")
        for enfant, sous_arbre in arbre['sous_arbres'].items():
            afficher_arbre(sous_arbre, niveau + 1)
main()
