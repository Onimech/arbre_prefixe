def creaAbr(m, k):
     A={'val' : 'R'}



def main ():
     motif = input("Entrez la motif : ")
     k = int(input("Entrez la longueur k : "))
     sequence = input("Entrez la séquence voulue :")
     alphabet = caracteres_diff(sequence)
     print(sequence)
     print(alphabet)

def caracteres_diff(seq):
     return(set(seq))
#for i in nbalphabet
#new fils"i"

#noeud des arbre : liste contenant le dernier caractere du motif et les positions du motif


#registe des derniers motifs rencontrés, ajout du caractère rencontré aux motifs
#elimination des motifs de longueur supérieure à k

main()