from itertools import cycle

count=0
for i in cycle('abcd'):
    if count==61:
        break
    else:
        print(i,end=' ')
        count+=1
