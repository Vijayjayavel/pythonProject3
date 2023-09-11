from itertools import count

for i in count(5,3):
    if i >100:
        break
    else:
        print(i,end=' ')