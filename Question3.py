# Question3. 
# Merge dictionaries a and b. The ansant dict must contain all items of 
# both dicts. If key is common then the value of key in ansant dict 
# must be the sum of value in a and b.
# a = {'x': 1, 'y': 2, 'z': 3}
# b = {'a': 4, 'b': 5, 'y': 6}


# solution3:-

a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}

def mergeDict(a, b):
  
  ans = {}
  
  for i in a:
    ans[i]= a[i]
    
  for i in b:
    if i in ans:
      ans[i] += b[i]
    else:
      ans[i] = b[i]
      
  return ans
  
print(mergeDict(a, b))
