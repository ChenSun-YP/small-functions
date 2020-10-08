#my little binary serch code
#Author: Chen Sun
from typing import List

def bs(list:List[int],x) ->int :

    list.sort()
    print(list)
    f = 0
    e = len(list)
    while (e>f):
        mid = (f + e) // 2

        if list[mid] < x:
            #go right
            f =mid
        elif list[mid] > x:
            e = mid
        else:
            return mid
    return -1


test =[3,2,4,5,6,78,1]
print(bs(test,3))

