# Created on iPad.

arr = [2,5,7,1,4,10,3,2,5]

def quicksort(arr,low,high):
    if high > low:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)



def partition(arr,low,high):
    i = low -1
    pivot = arr[high]

    for j in range (low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quicksort2(arr, low, high):
    if low < high:
        i, j = partition2(arr, low, high)

        quicksort2(arr, low, j)
        quicksort2(arr, i, high)


def partition2(arr, low, high):
    i = low
    j = high
    pivot = arr[(low + high) // 2]

    while i <= j:

        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i, j

def bucket_sort(arr):
    if len(arr) <= 1:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    bucket_count = len(arr)

    # Create one bucket per input element.
    buckets = [[] for _ in range(bucket_count)]

    # Avoid division by zero when all values are equal.
    if max_value == min_value:
        return arr

    # Distribute each value into its corresponding bucket.
    for value in arr:
        index = int(
            (value - min_value)
            / (max_value - min_value)
            * (bucket_count - 1)
        )
        buckets[index].append(value)

    # Sort the values within each bucket.
    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result

def distribution_sort(xs, key_function):
    if not xs:
        return []

    keys = []

    for x in xs:
        keys.append(key_function(x))

    min_key = min(keys)
    max_key = max(keys)

    number_of_blocks = max_key - min_key + 1

    blocks = []

    for _ in range(number_of_blocks):
        blocks.append([])

    for x in xs:
        key = key_function(x)
        index = key - min_key
        blocks[index].append(x)

    result = []

    for block in blocks:
        result.extend(block)

    return result

print(distribution_sort(arr,lambda x:x))
