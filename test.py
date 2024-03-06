

def main():
    k = int(input("Entrez la longueur k : "))
    sequence = input("Entrez la séquence voulue :")
    alphabet = caracteres_diff(sequence)
    liste_suffixe = [""]
    arbre = init_arbre(alphabet)
    remplissage_abr(sequence, arbre, alphabet, liste_suffixe, k)
    print(arbre)


def caracteres_diff(seq):
    return set(seq)

def init_arbre(alphabet):
    A = {}
    A["clé"] = 0
    for l in alphabet:
        A[l] = {}
    return A

def remplissage_abr(seq, arbre, alphabet, LS, k):
    for caractere in seq:
        if caractere in alphabet:
            LS[:] = [mot + caractere for mot in LS]
            LS.append("")
            for suffixe in LS:
                if len(suffixe)>k:
                    LS.remove(suffixe)
        
main()



            # if arbre[caractere] == {}:
            #     arbre[caractere] = {'clé': 1, 'T': {}, 'C': {}, 'G': {}, 'A': {}}  # Initialisez le compteur à 1
            # else:
            #     arbre[caractere]['clé'] += 1  # Incrémentation du compteur








main()
