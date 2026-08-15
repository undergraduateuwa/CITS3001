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

    # 找出最大值和最小值
    max_val = max(arr)
    min_val = min(arr)

    # 确定桶的数量
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # 将元素分配到桶中
    for num in arr:
        # 计算桶的索引
        index = int((num - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[index].append(num)

    # 对每个桶进行排序（这里使用内置排序）
    for bucket in buckets:
        bucket.sort()

    # 收集所有元素
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

    # 1. 统计每个数字出现次数
    for num in arr:
        count[num - min_val] += 1

    for value in range(len(count)):
        output.extend([value+min_val] * count[value])

    return output





if __name__ == "__main__":
    # 测试样例


    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))





