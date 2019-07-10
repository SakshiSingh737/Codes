# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    m=len(a)
    n=len(b)
    l=[[None]*(n+1) for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                l[i][j]=0
            elif(a[i-1]==b[j-1]):
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    index=l[m][n]
    print(index)
    temp=index
    lcs = [""] * (index+1) 
    i=m;j=n
    while(i>0 and j>0):
        if a[i-1] == b[j-1]: 
            lcs[index-1] = a[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif l[i-1][j] > l[i][j-1]: 
            i-=1
        else: 
            j-=1
    for k in lcs:
        print(k)
    return lcs
    
