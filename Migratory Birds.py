# Using List
# Complete the migratoryBirds function below.

def migratoryBirds(arr):
 l= [0,0,0,0,0,0]
    for i in arr:
        l[i] += 1
    k = max(l)
    return(l.index(k))



# Using Dictionary
# Complete the migratoryBirds function below.

def migratoryBirds(arr):
  l = list(arr)
  dic = {i:0 for i in l}
  for i in l:
    dic[i] += 1
  for key, value in sorted(dic.items(), key = itemgetter(1), reverse = True):
  return key
