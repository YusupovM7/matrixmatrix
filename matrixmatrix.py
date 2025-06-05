def fileopen(t):
    with open(t) as file:
        x = []
        for line in file:
            z = list(map(int,line.split(',')))
            x.append(z)
    return x
def matr(s):
    for i in range(0,5):
        print(s[i])
def cc(g,h,j,p):
    q=0
    for o in range(0,5):
        q=q+g[j][o]*h[o][p]
    return q


c=[[],[],[],[],[] ]

a=fileopen("a-matrix.txt")
b=fileopen("b-matrix.txt")
for x in range(0,5):
    for z in range(0,5):
        c[x].append(cc(a,b,x,z))

def __main__():
    matr(a)
    print('       *')
    matr(b)
    print('       =')
    matr(c)

    with open("c-matrix.txt", "w") as file:
        for i in range(0,5):
            file.write("\n")
            for j in range(0,5):
                s='' if j==4 else ','
                file.write(f'{c[i][j]}{s} ')

if __name__ == "__main__":
    __main__()
