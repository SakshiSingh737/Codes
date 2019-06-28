import os
import sys
import math
#
# Complete the restaurant function below.
#
def restaurant(l, b):
    x = math.gcd(l,b)
    return int(l/x*b/x)
    
# Rest of the part is same as given in the editor
