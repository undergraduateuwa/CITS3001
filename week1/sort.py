# Return a sorted copy using merge sort.
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

# Merge two sorted lists into one sorted list.
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



# Sort numeric values by distributing them into buckets.
def bucket_sort(arr):
    if not arr:
        return arr

    # 鎵惧嚭鏈€澶у€煎拰鏈€灏忓€?
    max_val = max(arr)
    min_val = min(arr)

    # 纭畾妗剁殑鏁伴噺
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # 灏嗗厓绱犲垎閰嶅埌妗朵腑
    for num in arr:
        # 璁＄畻妗剁殑绱㈠紩
        index = int((num - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[index].append(num)

    # 瀵规瘡涓《杩涜鎺掑簭锛堣繖閲屼娇鐢ㄥ唴缃帓搴忥級
    for bucket in buckets:
        bucket.sort()

    # 鏀堕泦鎵€鏈夊厓绱?
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Process one digit position for a counting-sort pass.
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    digits_records = [0 for _ in range(n)]

    for num in arr:
        digit = num // exp
        digits_records[digit] += 1




    return arr



# Sort non-negative integers with radix sort.
def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1

    while max_num/exp > 0:
        counting_sort_by_digit(arr,exp)
        exp *= 10

    return arr



# Sort values by counting their frequencies.
def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = []

    # 1. 缁熻姣忎釜鏁板瓧鍑虹幇娆℃暟
    for num in arr:
        count[num - min_val] += 1

    for value in range(len(count)):
        output.extend([value+min_val] * count[value])

    return output





if __name__ == "__main__":
    # 娴嬭瘯鏍蜂緥


    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
