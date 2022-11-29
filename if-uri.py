#: (if1)program care sa calculeze, (1)adunarea, (2)scaderea, (3)inmultirea, (4)impartire
#: (pb1)dat fiind un numar, incadrati-l in unul din domeniile mic(0-1000), mediu(1000-10000), mare(10000-infinit)
#: (sir5)se introduce de la tastatura un sir de numere. sa se verifice care element este egal cu 5.
#: Si sa se contorizeze aparitiile.

def adunare():
    print("a=", end=" ")
    a = int(input())
    print("b=", end=" ")
    b = int(input())
    print("a+b=", a+b)


def if1():
    print("Tastati 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire sau 4 pentru impartire:")
    o = input().strip()
    if o == "1":
        print("adunare")
        adunare()
    else:
        if o == "2":
            print("scadere")
        else:
            if o == "3":
                print("inmultire")
            else:
                if o == "4":
                    print("impartire")
                else:
                    print("Introduceti doar 1, 2, 3 sau 4")


def pb1():
    print("Introduceti va rog un numar natural:", end="")
    a = int(input())
    if a < 0:
        print("introduceti va rog un numar natural")
    else:
        if a < 1000:
            print("valoare mica")
        else:
            if a < 10000:
                print("valoare medie")
            else:
                print("valoare mare")


def sir5():
    print("Introduceti sirul de numare naturale de forma '25412563':")
    sir = input()
    contor = 0
    for caracter in sir:
        if caracter == "5":
            contor += 1
    print(contor)


def lista5():
    lista = [5, 4, 6, 5, 1, 6, 9, 7, 5, 6]
    contor = 0
    for index in range(len(lista)):
        if lista[index] == 5:
            contor += 1
    print(contor)


if __name__ =="__main__":
    pb1()
    sir5()
    lista5()