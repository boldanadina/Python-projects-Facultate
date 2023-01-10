#recapitulare
def parcurgere_lista():
    l1=list()
    for i in range(len(l1)):
        print(l1[i])
    for element in l1:
        print(element)


def dictionar():
    dict1={'zi':'day', 'noapte':'night', 'buna ziua':'hello'}
    for element in dict1.keys():
        print(element)


def dictionar2():
    dict2={'a':1,'b':2,'c':3,'d':4,'e':2,'f':6,'g':3,'h':7,'i':1,'j':4}
    s=0
    element=input()
    for i in range(len(element)):
        s=s+dict2[element[i]]
    print(s)

if __name__=="__main__":
    dictionar()
    dictionar2()