# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma_numere():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)

    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('suma numerelor a si b este a+b , adica', a+b)

def inmultirea_numere():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)

    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('inmultirea numerelor a si b este a*b , adica', a*b)

def impartirea_numere():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('impartirea numerelor a si b este a/b , adica', a/b)

def diferenta_numere():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('diferenta numerelor a si b este a-b , adica', a - b)

def perimetru():
    print('introduceti prima latura, ab')
    ab=int(input())
    print('prima latura ab=' , ab)
    print('introduceti a doua latura, bc')
    bc=int(input())
    print('a doua latura bc=' , bc)
    print('introduceti a treia latura, ac')
    ac=int(input())
    print('a treia latura ac=' , ac)
    print('perimetrul triunghiului este ab+bc+ac= , adica ' , ab+bc+ac)

def aria():
    print('introduceti baza, ab')
    ab=int(input())
    print('baza ab=' , ab)
    print('introduceti inaltimea, bc')
    bc=int(input())
    print('inaltimea bc=' , bc)
    print('aria numerelor ab si bc este=(ab*bc)/2= , adica ' , (ab*bc)/2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    suma_numere()
    inmultirea_numere()
    impartirea_numere()
    diferenta_numere()
    perimetru()
    aria()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
