# In this file two solutions are provided for the given problem statement, first: using LOOPS,
# second: using Python String center()|ljust()|rjust(). 

# (1) Using Loops

import math
n = input().split()
k = math.ceil(int(n[0])/2)
for i in range(k-1):
    pt = 3*(i+(i+1))
    ds = int((int(n[1])-pt)/2)
    for l in range(ds):
        print("-",end="")
    pt2 = int(pt/3)
    for l2 in range(pt2):
        print(".|.",end="")
    for l in range(ds):
        print("-",end="")
    print()

t1 = int((int(n[1])-7)/2)
for i in range(t1):
    print("-",end="")
print("WELCOME",end="")
for i in range(t1):
    print("-",end="")
print()

pt1= int(n[1])
for i in range(k-1):
    pt1 = pt1 - 6
    ds1 = int((int(n[1])-pt1)/2)
    for l in range(ds1):
        print("-",end="")
    pt3 = int(pt1/3)
    for l2 in range(pt3):
        print(".|.",end="")
    for l in range(ds1):
        print("-",end="")
    print()

        
# (2) Using Python String | ljust(), rjust(), center()

n,m=map(int,input().split())
for i in range(1,n,2):
    print(str('.|.'*i).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n-2,-1,-2):
    print(str('.|.'*i).center(m,'-'))
