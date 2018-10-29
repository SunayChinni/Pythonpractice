l1 = [10,20,30,40,50]
l2 = l1
l2[2] = 90
print(l1)
print(l2)

import copy as cp
l1 = [10,20,30,40,50]
l2 = cp.copy(l1)
l2[2] = 90
print(l1)
print(l2)

l1 = [[10,20,30],[40,50,60]]
print(l1)
print(l1[0])
print(l1[1][2])

import copy as cp
l1 = [[10,20,30],[40,50,60]]
l2 = cp.copy(l1)
l2[1][2] = 90
print(l1)
print(l2)

import copy as cp
l1 = [[10,20,30],[40,50,60]]
l2 = cp.deepcopy(l1)
l2[0][1] = 90
print(l1)
print(l2)