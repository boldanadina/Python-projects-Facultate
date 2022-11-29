def matrice1():
    matrice = []
    col = 2
    rand = 3
    for i in range(rand):  # repeta pt fiecare rand
        m_col = []  #: definesc elementele care va contine elem. de pe coloanele matricii sale
        #: lista este def pt fiecare rand in parte
        for j in range(col):
            print("[", i, '][', j, ']', end=' ')
            if i == j:
                print("element de pe diagonala principala")
            element = input()
            m_col.append(element) # se preia elem corespunzator coloanei j al randului curent
        # dupa ce am terminat de preluat toate coloanele, adaug randul respectiv la matrice
        matrice.append(m_col)
    for i in range(rand):
        for j in range(col):
            print("[", i, ',', j, '=', matrice[i][j], end=']')
        print("")


if __name__ == "__main__":
    matrice1()




#: tema: de calculat suma elementelor de pe diagonala principala
#: suma pt fiecare rand si suma pt fiecare coloana