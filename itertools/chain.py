from itertools import chain

def flatten_list(*list1):
    return list(chain(*list1))

print(flatten_list([1,2,3,4],[6,55,6,6,3424,542]))