def creaAbr(m, k):
     A={'val' : 'R'}



def main ():
     motif = input("Entrez la motif : ")
     k = input("Entrez la longueur k : ")
     sequence = input("Entrez la séquence voulue :")
     alphabet = caracteres_diff(sequence)
     print(sequence)
     print(alphabet)

def caracteres_diff(seq):
     return(set(seq))


main()