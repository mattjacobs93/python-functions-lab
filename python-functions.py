#1 sum to:

def sum_to(n:int) -> int:
  return n*(n+1)//2


print('#1 - Sum to 100 is: ',sum_to(100))

#2 largest:

def largest(lst):
  return max(lst)

print('Largest is: ', largest([10, 4, 2, 231, 91, 54]))

#3 occurrences:

def occurrences(str1,str2):
  return str1.count(str2)


print('Num occurences: ', occurrences('fleep floop', 'e'))

#4 product:
from functools import reduce
def product(*args):
  return reduce(lambda a,b: a*b,args,1)

print('Product: ', product(2, 5, 5))