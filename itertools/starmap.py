import itertools
x=[[1,2,3],[43,2,3],[334,55,66,543]]
print(list(itertools.starmap(min,x)))