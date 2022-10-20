import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt('signal02.dat', float)
arr = np. array(a)

arr1 = np.zeros(len(arr))
for i in range(len(arr)):
    if i < 10:
        arr1[i] = sum(arr[0:i + 1]) / (i + 1)
    else:
        arr1[i] = sum(arr[i - 9:i + 1]) / 10

plt.plot(arr1)
plt.show()