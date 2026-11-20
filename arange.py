import numpy as np

a1 = np.array([1,2,3])
#print(a1)

# arange function makes an array on equal distance

a2 = np.arange(10,100,10) # 10 included and 100 is excluded
# arange(start : stop : steps)
print(a2)

a3 = np.arange(-9, 9, 0.5)
# arange(start : stop : steps)
# include start. exclude stop in output
print(a3)

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(np.power(a1, a2)) # a1^a2
