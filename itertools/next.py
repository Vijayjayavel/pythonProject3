import itertools

it=itertools.cycle(['daf','afdv','asfv'])
for i in range(10):
    print(next(it),end=' ')