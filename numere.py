def adunarecifre2():
    print("introduceti va rog un numar de doua cifre:")
    a = input()
    a = int(a)
    z = a // 10
    u = a % 10
    print("suma zecilor si unitatilor este:", z+u)

def adunarecifre3():
    print("introduceti va rog un numar de trei cifre:")
    a = input()
    a = int(a)
    s = a // 100
    z = (a // 10)%10
    u = a % 10
    print("suma zecilor unitatilor si sutelor este:", z + u + s)


def capetepicioare():
    print("introduceti numarul de gaini :")
    g = int(input())
    print("introduceti numarul de oi :")
    o = int(input())
    print("numarul de capete este:" , g+o , "iar numarul de picioare este: ", 2*g+4*o)



def capetepicioare2():
    print("introduceti numarul de picioare :")
    p = int(input())
    print("introduceti numarul de capete :")
    c = int(input())
    o = (p-2*c)//2
    g = c-o
    print("numarul de oi este:" , o  , "iar numarul de gaini este: ", g)

def eliminarecifra():
    print("introduceti va rog un numar de trei cifre:")
    a = input()
    a = int(a)
    s=a//100
    z = (a // 10) % 10
    u= a%10
    print("numarul obtinut prin eliminare este:", s*10+u )

def cub():
    print("introduceti va rog latura cubului:")
    a = input()
    a = int(a)
    s = 6*a*a
    v = a**3
    print("suprafata cubului este:", s , "iar volumul este:" , v )

def produs():
    print("Introduceti va rog un numar de 3 cifre:")
    a = int(input())
    s = a // 100
    u = a % 10
    print("Produsul cifrelor numarului este:", s * u)


def suma_gauss():
    print("Introduceti un numar n:")
    n = int(input())
    s = (n*(n+1)) // 2
    print("Suma primelor n numere naturale este:", s)


def patrat_nr():
    print("Introduceti un numar de trei cifre:")
    a = int(input())
    s = a // 100
    u = a % 10
    b = s * 10 + u
    print("Patratul numarul nou este:", b ** 2)







if __name__ == "__main__":
    adunarecifre2()
    adunarecifre3()
    capetepicioare()
    capetepicioare2()
    eliminarecifra()
    cub()
    produs()
    suma_gauss()
    patrat_nr()
