def tri_sup(l,b):
    x=l[len(l)-1][len(l)-1]/b[len(l)-1]


    for i in range(1,len(l)):
        i+=i
        print(x)
        for j in range(1,len(l)):
            x=(1/l[i][i])*(x-l[i][j]*x)
            print(x)
            return x
mat=[[2,1,-1],[0,1/2,1/2],[0,0,-1]]
vect=[8,1,1]
print(tri_sup(mat,vect))
print(len(mat))