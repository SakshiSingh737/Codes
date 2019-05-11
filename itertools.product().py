from itertools import product
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l1=list(product(n,m))
for i in l1:
    print(i,end=" ")
