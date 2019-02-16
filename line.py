N=input()
B=[]
for _ in range(int(N)):
    a=input().split()
    a[0]=int(a[0])
    a[1]=int(a[1])
    B.append(a)
    B[_].append(_)
B1=sorted(B)
grap={}
for _ in range(int(len(B))):
    i=_+1
    C=[]
    while(i<int(len(B))):
        if B[_][1]<B[i][0]:
            break
        C.append(B[i][2])
        grap[B[_][2]]=set(C)
        i=i+1
ngrap=[]
for _ in range(int(len(B))):
    ngrap.append([])
for _ in grap.keys():
    for a in grap[_]:
        ngrap[_].append(a)
    for a in grap[_]:
        ngrap[a].append(_)
def extractMin(S,d):
    a={}
    for _ in S:
        a[d[_]]=_
        b=list(a.keys())
    return a[min(b)]
def Dijkstra(G,r,a):
    S=set([])
    d=list(range(int(len(G))))
    for u in range(int(len(G))):
        d[u]=150001
    d[r]=0
    V=set(list(range(int(len(G)))))
    while(S!=V):
        u=extractMin(V-S,d)
        S=S.union({u})
        for v in G[u]:
            if(set()!={v}&(V-S) and d[u]+1<d[v]):
                d[v]=d[u]+1
    doon=[]
    for _ in S:
        doon.append(d[_])
    if doon[a-1]==150001:
        return -1
    return doon[a-1]
def quest(a,b):
    print(Dijkstra(ngrap,a-1,b))

N2=input()
for _ in range(int(N2)):
    a,b=input().split()
    a=int(a)
    b=int(b)
    quest(a,b)
   
