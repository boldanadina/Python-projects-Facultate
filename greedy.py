def spectacol(lista): #lista ne va fi de forma: [ [1,8], [8,12], [8,10]...]
    lista=sorted(lista, key=lambda el: el[1])
    final=[lista[0]]
    ultimaora=lista[0][1]
    for el in specs:
        if el[0]>=ultimaora:
            final.append(el)
    print("numar spectacole: ", len(final))


if __name__=="__main__":
    #specs=list()
    # n= int(input("numar spectacole:"))
    #for i in range(n):
        #oi=int(input(ora in."))
        #os=int(input("ora sf."))
        #specs.append([oi, os])
    specs=[[1,8], [8,10], [8,12], [12,13], [15,17], [18,21], [17,20]]
    spectacol(specs)


