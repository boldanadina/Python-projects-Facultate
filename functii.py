sm: int = 0

def suma(a, b):
    print("2", a+b)
    return a+b

def suma1(*args):
    print(args)
    s = 0
    for x in args:
        s += x
    return s

def sumametoda(*args):
    global sm
    s = 0
    for a in args:
        s += a
    sm = s

def gauss(n):
    # n*(n+1)/2
    g = n*(n+1)//2
    return g

#de realizat o functie care extrage primele 5 elemente dintr-o lista
def extragere5(lista):
    listarezultat = list()
    for index in range (len(lista)):
        if index <5:
            listarezultat.append(lista[index])
    return listarezultat

def suma_div(n, s):
    for i in range(1, n+1):
        if n%i == 0:
            s = s+i
    return s

def suma_cifrelor(n, s_cifre):
    while n> 0:
        s_cifre += n
        n = n-1
    return s_cifre

def produs(*args):
    print(args)
    p = 1
    for x in args:
        p = p * x
    return p

if __name__ == "__main__":
    print("1", suma(2, 3))
    print("program principal pas 2:", suma1(2, 3, 4, 5, 6, 7))
    #apel functie, la variabila c ii  atribui rezultatul functiei suma
    c = suma1(2, 3, 4, 5)
    print(c)
    sumametoda(sm, 2, 3, 4, 5, 6)
    print(sm)
    n=int(input("valoarea lui n:"))
    print(gauss(n))
    print(extragere5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    n = int(input("n="))
    print(suma_div(n,0))
    print(suma_cifrelor(n, s_cifre=0))
    print("valoarea produsului nr este :", produs(2, 3, 4, 5))


