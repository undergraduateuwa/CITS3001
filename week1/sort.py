def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(right, left)
    else:
        return arr

def merge(right,left):
    res = []
    i = 0
    j = 0
    while j < len(left) and i < len(right):
        if(right[i]>=left[j]):
            res.append(left[j])
            j += 1
        else:
            res.append(right[i])
            i += 1
    res.extend(left[j:])
    res.extend(right[i:])

    return res



def bucket_sort(arr):
    if not arr:
        return arr

    # Find the maximum and minimum values.
    max_val = max(arr)
    min_val = min(arr)

    # Use one bucket per input element.
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute each value into its corresponding bucket.
    for num in arr:
        # Map the value proportionally to a bucket index.
        index = int((num - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[index].append(num)

    # Sort each bucket with Python's built-in sort.
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets.
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    digits_records = [0 for _ in range(n)]

    for num in arr:
        digit = num // exp
        digits_records[digit] += 1




    return arr



def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1

    while max_num/exp > 0:
        counting_sort_by_digit(arr,exp)
        exp *= 10

    return arr



def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = []

    # Count the frequency of each value.
    for num in arr:
        count[num - min_val] += 1

    for value in range(len(count)):
        output.extend([value+min_val] * count[value])

    return output





if __name__ == "__main__":
    # Example run.


    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
