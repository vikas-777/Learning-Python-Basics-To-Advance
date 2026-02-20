import numpy as np
def standard_deviation(arr):
    mean = arr.mean()
    final_val=0
    for i in arr:
        val = (i-mean)**2
        final_val += val
    return (final_val/len(arr))**0.5
arr = np.array([1,3,5,7,9])
print(standard_deviation(arr))

values = np.array([1,3,5,7,9])
sd= standard_deviation(values)
print(sd)
