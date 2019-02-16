def a():
    c=input().split()
    if len(c)>len(list(range(0,int(C)))):
        a()
    else:
        return c

final=input()
for f in range(0,int(final)):
    m_num=input()
    group=[]
    for num in range(0,int(m_num)):
        R,C=input().split()
        c=[]
        c=a()
        c_perR=[]
        for c1 in c:
            c_perR.append(float(c1)/float(R))
        group.append(c_perR)
    maxs=list(range(0,len(group)))
    for m in range(0,len(maxs)):
        maxs[m]=0.0
    cot=list(range(0,int(m_num)))
    lenn=0
    for g in group:
        lenn=lenn+len(g)

    if lenn>10:
        for m in range(0,len(maxs)):
            maxs[m]+=max(group[m])
            group[m].remove(max(group[m]))
        while 10>len(cot):
            minn=maxs.index(min(maxs))
            if len(group[minn])==0:
                break
            maxs[minn]+=max(group[minn])
            group[minn].remove(max(group[minn]))
            cot.append(3)
        print(int(min(maxs)))
    else:
        ss=[]
        for g in group:
            s=0
            for g1 in g:
                s+=g1
            ss.append(s)
        print(int(min(ss)))
