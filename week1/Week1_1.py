# Created on iPad.
# Return the maximum subarray sum using Kadane's algorithm.
def notnaive(arr):
    cursum = 0
    res = 0
    j = 0
    for num in arr:
        cursum += num
        if cursum > res:
            res = cursum
        if cursum < 0:
            cursum = 0
    return res

arr = [1,2,3,-5,7,9,-29,20]
print(notnaive(arr))
