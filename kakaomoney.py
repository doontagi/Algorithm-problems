def gcd(m,n): #최대 공약수 함수, 유클리드 호제법
    return gcd(n,m%n) if n else m
N=input() # 로그 갯수
a=list(range(300003)) # 입출금내역
b=list(range(300003)) # 잔고
num=0 # 최대공약수
for i in range(int(N)):
    i=i+1
    A=input().split()
    a[i]=int(A[0])
    b[i]=int(A[1])
    num=gcd(num,b[i]-b[i-1]-a[i])
i=1
lis=range(int(N))
for i in lis:
    i=i+1
    if(b[i]-b[i-1]==a[i]):
        continue
    if((num and num <= b[i]) or a[i]>0 or (a[i]<0 and -a[i]<b[i-1])):
        print(-1)
        exit()
print(num if num else 1)
