# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt=0
    n = len(c)-1
    i=0
    while(i<n):
        if(i+2<=n and c[i+2]==0):
            i+=2
            cnt+=1
        elif(i+1<=n and c[i+1]==0):
            i+=1
            cnt+=1
    return cnt
