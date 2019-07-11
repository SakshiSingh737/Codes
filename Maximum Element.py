n = int(input())
l=[]
mx=[-999] 
for i in range(n):
    k=list(map(int,input().split()))
    p=k[0]
    if(p==1):
        n1=k[1]
        if(n1>=mx[len(mx)-1]):
            mx.append(n1)
        
        l.append(n1)
    elif(p==2):
        x=l.pop()
        if(x==mx[len(mx)-1]):
            mx.pop()
            
    else:
        print(mx[len(mx)-1])
