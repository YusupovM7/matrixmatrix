def matr(s):
    for i in range(0,5):
        print(s[i])

def cc(g,h,j,p):
    q=0
    for o in range(0,5):
        q=q+g[j][o]*h[o][p]
    return q

a=[[1,2,3,1,2],
   [2,3,2,2,-1],
   [3,2,1,-2,2],
   [-3,2,1,4,2],
   [3,4,-4,2,0]]

b=[[2,1,3,4,2],
   [3,4,2,6,2],
   [1,2,3,2,-1],
   [3,5,3,2,1],
   [2,4,2,4,1]]

c=[[],[],[],[],[]]

for x in range(0,5):
    for z in range(0,5):
        c[x].append(cc(a,b,x,z))


matr(a)
print('       *')
matr(b)
print('       =')
matr(c)    