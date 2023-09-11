from itertools import permutations

print(list(permutations([3,'python',34],2)))
#[(3, 'python'), (3, 34), ('python', 3), ('python', 34), (34, 3), (34, 'python')]

print(list(permutations([3,'python',34],3)))
#[(3, 'python', 34), (3, 34, 'python'), ('python', 3, 34), ('python', 34, 3), (34, 3, 'python'), (34, 'python', 3)]

print(list(permutations('vijay')))

print(list(permutations(range(4,10),3)))