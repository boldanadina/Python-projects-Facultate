def suma():
    n=4
    matrice=[[0]*n for _ in range(n)]
    s1=0
    s2=0
    for i in range(4):
        for j in range(4):
            print(i,",",j,end="=")
            matrice[i][j]=int(input())
            if i<j:
                s1=s1+matrice[i][j]
            if i+j<n:
                s2=s2+matrice[i][j]
    print("")
    print("suma diagonala principala=",s1)
    print("suma diagonala secundara=",s2)

def pb2():
    n=4
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j]=matrice[i][j]**2
    for i in range(n):
        for j in range(n):
            print(matrice[i][j],end=" ")
        print("")


def pb3():
    n=4
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j]=matrice[i][j]+2
    for i in range(n):
        for j in range(n):
            print(matrice[i][j],end=" ")
        print("")

if __name__ == "__main__":
    suma()
    pb2()
    pb3()
