import os
import sys
def stacks(t1,t2,t3):
    i=len(t1)
    j=len(t2)
    k=len(t3)
    while(i>0 and j>0 and k>0):
        if(t1[i-1] == t2[j-1] and t2[j-1] == t3[k-1]):
            return t1[i-1]
        elif(t1[i-1] > t2[j-1] or t1[i-1] > t3[k-1]):
            t1.pop()
            i-=1
        elif(t2[j-1] > t1[i-1] or t2[j-1] > t3[k-1]):
            t2.pop()
            j-=1
        elif(t3[k-1] > t2[j-1] or t3[k-1] > t1[i-1]):
            t3.pop()
            k-=1
    return 0
        

n1, n2, n3 = (map(int,input().split()))
l1=list(map(int, input().split()))[::-1]
l2=list(map(int, input().split()))[::-1]
l3=list(map(int, input().split()))[::-1]
for i in range(1,len(l1)):
    l1[i] = l1[i]+l1[i-1]
for i in range(1,len(l2)):
    l2[i] = l2[i]+l2[i-1]
for i in range(1,len(l3)):
    l3[i] = l3[i]+l3[i-1]
x=stacks(l1,l2,l3)
print(x)
