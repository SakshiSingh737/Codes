#In this find the GCD of the given elements in list 'a' if its gcd is 1, it means there is no element which can divide all. Hence, it contains a subset
# Complete the solve function below.
def solve(a):
    res = a[0]
    for i in range(1,len(a)):
        res = math.gcd(a[i],res)
    if(res != 1):
        return 'NO'
    else:
        return 'YES'
