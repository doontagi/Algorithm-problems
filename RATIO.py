T=input()
for _ in range(int(T)):
    M,N=input().split()
    M=int(M)
    N=int(N)
    r=float(M-N)
    b=int((100*N/M)+ (0.01 *100))
    if(b==100):
        print(-1)
    else:
        c=float(100*r/(100-b))
        if(r==0):
            print(-1)
        elif(((c-M)%1.0)==0):
            if((int(c-M))>2000000000):
                print(-1)
            else:
                print(int(c-M))
        else:
            if((int(c-M)+1)>2000000000):
                print(-1)
            else:
                print(int((c-M)+1))
