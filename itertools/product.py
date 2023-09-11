# cartesian product of input iterables
from itertools import product

print(list(product([1,2,3],repeat=3)))

print(list(product(['vijay','kali'],'8','9')))

print(list(product('c',[5,7])))