import math


def cautare():
    lista = [100, 56, 20, 10, 30, 45, 6, 47, 12, 10]
    val = int(input())
    suma = 0
    for i in range(len(lista)):
        if lista[i] == val:
            print("Indicele pentru valoarea cautata=", i)
    for i in range(3, 8, 1):
        suma += lista[i]
    print("Suma nr este", suma)



def cautare_salt():
    l = [100, 56, 20, 10, 30, 45, 6, 47, 12, 10]
    #cauatrea cu salt nu merge fara sortare
    val=30
    l.sort() # am sortat lista
    ls=l
    print(ls)
    n = len(ls)
    st = 0
    salt = int(math.sqrt(n))
    # identificam portiunea din lista in care se gaseste elementul pe care dorim sa-l cautam
    for i in range(0, n, salt):
        if ls[i]<val:
            st = i
        elif ls[i] == val:
            print(i)
        else:
            break
    # cautarea secventiala in bucata identificata
    for i in range(st, st+salt):
        if ls[i] == val:
            print(i)


if __name__ == "__main__":
    #cautare()
    cautare_salt()

    