from itertools import combinations

print(list(combinations('123',2)))
#[('1', '2'), ('1', '3'), ('2', '3')]
print(list(combinations([1,2,3,4,5],3)))
#[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
print(list(combinations(range(9),4)))