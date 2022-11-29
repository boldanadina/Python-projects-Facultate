def lista1():
    lista = [100, 10, 20, 34, 200, 150]
    print(lista)
    print("tiparire lista folosind 'in'")
    for element in lista:
        print(element, end=",")
    print("")
    print("tiparire lista folosind range:")
    for index in range(len(lista)):
        print(lista[index], end=",")
    print("")
    lista.append(210)
    lista.append(23)
    print(lista)
    lista.pop()
    print("")
    print(lista)
    print("Max=", max(lista))
    print("Min=", min(lista))


def stiva1():
    from collections import deque
    stiva = deque()
    stiva.append(100)
    stiva.append(10)
    stiva.append(20)
    stiva.append(34)
    stiva.append(200)
    stiva.append(150)
    for element in stiva:
        print(element, end=',')
    print("")
    stiva.append(210)
    print(stiva)
    print("")
    stiva.append(23)
    print(stiva)
    print("")
    stiva.pop()
    print(stiva)


if __name__ == "__main__":
    lista1()
    stiva1()