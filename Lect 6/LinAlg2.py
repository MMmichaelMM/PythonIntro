import numpy as np
# A = np.random.randint(1, 6, 4)  # 4 integers from [1, 6)
# B = np.random.randint(1, 6, (4, 4))  # 4x4 matrix integers from [1, 6)
# print(A)
# print(B)

C = np.random.randint(1, 10, size=(4, 4))
print(C)
print('')
# print(len(C))
# print(C.shape)
# print(type(C.shape))
# print('')
# print(C[1:, 2:])
# print('')
# print(C[[0, 2]][:, [0, 1, 3, 4]]) #Slicing non-continous indexes
# print('')
# print(C[2:][:, [0, 1, 3, 4]]) #Slicing non-continous indexes
print('')
# print(C[[0,1,3]][:, [0,1,3]]) #Slicing non-continous indexes
i=0
# print(C[1:][:, i:]) #Slicing non-continous indexes
print(np.hstack((C[1:, :i], C[1:, i+1:])))



