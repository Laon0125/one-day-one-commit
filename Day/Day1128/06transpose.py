import numpy as np

a = np.array(
    [
        [1,2,3],
        [7,8,9]
    ]
)

print (np.transpose(a))
print (a.T) # same as np.transpose(a)
print()
'''
[
    [1,7]
    [2,8]
    [3,9]
]
'''