import itertools

import operator

print(list(itertools.accumulate([1,2,3,4,5,6])))

print(list(itertools.accumulate([1,2,3,4,5,6],operator.mul)))

print(list(itertools.accumulate([2,3,5,9],operator.mod)))

print(list(itertools.accumulate([1,2,3,4,5,6,0],operator.le)))
