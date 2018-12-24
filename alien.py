def find(n,Ms,Ma,point,remains):
    a=0
    for i in range(int(len(Ms))):
        if(Ma[i]==0):
            continue
        elif(Ms[i]==n):
            a=a+Ma[i]
            Ma[i]=0
            continue
        else:
            if((n-Ms[i]) in Ms):
                if((n-Ms[i])==Ms[i]):
                    if(Ma[Ms.index(n-Ms[i])]==1):
                        continue
                    a=a+int(Ma[i]/2)
                    Ma[i]=Ma[i]%2
                    continue
                if(Ma[i]>Ma[Ms.index(n-Ms[i])]):
                    a=a+Ma[Ms.index(n-Ms[i])]
                    Ma[Ms.index(n-Ms[i])]=0
                    Ma[i]=Ma[i]-Ma[Ms.index(n-Ms[i])]
                    continue
                else:
                    a=a+Ma[i]
                    Ma[i]=0
                    Ma[Ms.index(n-Ms[i])]=Ma[Ms.index(n-Ms[i])]-Ma[i]
                    continue
    point[0]=point[0]+n*a
    return(a,point)
T=input()
for z in range(int(T)):
    N,M,B=input().split()
    Ms=[]
    Ma=[]
    Mr=[]
    N=int(N)
    NN=[N]
    C=NN[:]
    B=int(B)
    M=int(M)
    for i in range(M):
        A=input().split()
        Ms.append(int(A[0]))
        Ma.append(int(A[1]))
    for i in range(M):
        Mr.append([Ms[i],Ma[i]])
    point=[0]
    remains=Ms[:]
    BB=(B-1)*2
    if(B==1):
        BB=1
    while(N>0):
        N=N-find(B,Ms,Ma,point,remains)[0]
        B=B+1
        if(N<0):
            point[0]=point[0]+N*(B-1)
            break
        if(B>BB):
            for _ in range(int(len(Ms))):
                if(Ma[_]==0 and Ma[_] in remains):
                    remains.remove(Ma[_])
            remainsc=remains[:]
            for _ in range(int(len(remains))):
                if(remains[_]<BB):
                    remainsc.remove(remains[_])
            remains=remainsc
            if(remains==[]):
                break
            while (max(remains)>BB):
                ma=min(remains)
                indx=Ma[Ms.index(ma)]
                if(Ma[Ms.index(ma)]<N):
                    point[0]=point[0]+ma*Ma[Ms.index(ma)]
                else:
                    point[0]=point[0]+ma*N
                N=N-Ma[Ms.index(ma)]
                remains.remove(ma)
                if (remains==[] or N<1):
                    break
            break
    if N>0:
        print('#',end="");print(z+1,end=" ");print(-1)
    else:
        print('#',end="");print(z+1,end=" ");print(point[0])
