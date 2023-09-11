import itertools
list1 = [2, 4, 5, 7, 8,10,15,18,22]
# using dropwhile() iterator that will print start displaying after condition is false
print(list(itertools.dropwhile(lambda x: x % 2 == 0, list1)))
# vice versa to dropwhile
print(list(itertools.takewhile(lambda x:x%2==0,list1)))
print(list(itertools.filterfalse(lambda x: x % 2 == 0, list1)))



