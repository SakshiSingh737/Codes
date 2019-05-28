# Complete the toys function below.
def toys(w): 
    w.sort()
    n = len(w)
    j=i=s=0
    t=1
    while(i < n):
        k = w[j]+4
        if(w[i] <= k):
            s += 1
            i += 1
        else:
            t += 1
            j = s
    return t
