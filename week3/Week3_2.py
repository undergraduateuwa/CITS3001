# Created on iPad.
arr = [711,170,343,7,452,617,144,417]
def buck_sort(arr):
    res = 0
    return result



def radix_sort(arr):
    if not arr:
        return arr

    # 找到数组中的最大值，确定最多需要排多少位
    max_num = max(arr)

    # exp 表示当前处理的数位
    # exp = 1：个位
    # exp = 10：十位
    # exp = 100：百位
    exp = 1

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp):
    n = len(arr)

    # 临时结果数组
    output = [0] * n

    # 0~9 共 10 个桶
    count = [0] * 10

    # 统计当前数位上每个数字出现的次数
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # 转换为累计位置
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 必须从右向左放入 output，保证排序稳定
    for i in range(n - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % 10

        output[count[digit] - 1] = num
        count[digit] -= 1

    # 把结果复制回原数组
    for i in range(n):
        arr[i] = output[i]




def quick_select(arr,key,upper,lower):
    pivot = partition(arr,upper,lower)
    if pivot == key - 1:
        return arr[pivot]

    if key - 1 < pivot:
        return quick_select(arr,key,pivot-1,lower)
    
    else:
        return quick_select(arr,key,upper,pivot+1)


def partition(arr, upper, lower):
    current = arr[lower:upper + 1]

    # 找到一个保证 good split 的 pivot 值
    pivot_value = median_of_medians(current)

    # 找到这个 pivot 在原数组当前区间中的位置
    pivot_index = arr.index(pivot_value, lower, upper + 1)

    # 把 pivot 移动到最后
    arr[pivot_index], arr[upper] = arr[upper], arr[pivot_index]

    i = lower - 1

    for j in range(lower, upper):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[upper] = arr[upper], arr[i + 1]

    return i + 1

def median_of_medians(arr):
    # Base case：5 个或更少，直接排序并找中位数
    if len(arr) <= 5:
        sorted_arr = sorted(arr)
        return sorted_arr[len(sorted_arr) // 2]

    medians = []

    # 每 5 个元素分成一组
    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        group.sort()

        group_median = group[len(group) // 2]
        medians.append(group_median)

    return median_of_medians(medians)

print(quick_select(arr,4,7,0))


