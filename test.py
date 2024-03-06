

def main():
    k = int(input("Entrez la longueur k : "))
    sequence = input("Entrez la séquence voulue :")
    alphabet = caracteres_diff(sequence)
    liste_suffixe=[""]
    arbre = init_arbre(alphabet)
    print(arbre)
  


def caracteres_diff(seq):
    return set(seq)


def init_arbre(alphabet):
    A = {}
    A["clé"] = 0
    for l in alphabet:
        A[l]={}
    return A





main()
