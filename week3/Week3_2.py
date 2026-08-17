# Created on iPad.
arr = [711,170,343,7,452,617,144,417]
# Placeholder for a bucket-sort exercise.
def buck_sort(arr):
    res = 0
    return result



# Sort non-negative integers with radix sort.
def radix_sort(arr):
    if not arr:
        return arr

    # 鎵惧埌鏁扮粍涓殑鏈€澶у€硷紝纭畾鏈€澶氶渶瑕佹帓澶氬皯浣?
    max_num = max(arr)

    # exp 琛ㄧず褰撳墠澶勭悊鐨勬暟浣?
    # exp = 1锛氫釜浣?
    # exp = 10锛氬崄浣?
    # exp = 100锛氱櫨浣?
    exp = 1

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


# Process one digit position for a counting-sort pass.
def counting_sort_by_digit(arr, exp):
    n = len(arr)

    # 涓存椂缁撴灉鏁扮粍
    output = [0] * n

    # 0~9 鍏?10 涓《
    count = [0] * 10

    # 缁熻褰撳墠鏁颁綅涓婃瘡涓暟瀛楀嚭鐜扮殑娆℃暟
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # 杞崲涓虹疮璁′綅缃?
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 蹇呴』浠庡彸鍚戝乏鏀惧叆 output锛屼繚璇佹帓搴忕ǔ瀹?
    for i in range(n - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % 10

        output[count[digit] - 1] = num
        count[digit] -= 1

    # 鎶婄粨鏋滃鍒跺洖鍘熸暟缁?
    for i in range(n):
        arr[i] = output[i]




# Return the one-based selected order statistic.
def quick_select(arr,key,upper,lower):
    pivot = partition(arr,upper,lower)
    if pivot == key - 1:
        return arr[pivot]

    if key - 1 < pivot:
        return quick_select(arr,key,pivot-1,lower)

    else:
        return quick_select(arr,key,upper,pivot+1)


# Partition a slice and return the pivot position.
def partition(arr, upper, lower):
    current = arr[lower:upper + 1]

    # 鎵惧埌涓€涓繚璇?good split 鐨?pivot 鍊?
    pivot_value = median_of_medians(current)

    # 鎵惧埌杩欎釜 pivot 鍦ㄥ師鏁扮粍褰撳墠鍖洪棿涓殑浣嶇疆
    pivot_index = arr.index(pivot_value, lower, upper + 1)

    # 鎶?pivot 绉诲姩鍒版渶鍚?
    arr[pivot_index], arr[upper] = arr[upper], arr[pivot_index]

    i = lower - 1

    for j in range(lower, upper):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[upper] = arr[upper], arr[i + 1]

    return i + 1

# Select a robust pivot with the median-of-medians method.
def median_of_medians(arr):
    # Base case锛? 涓垨鏇村皯锛岀洿鎺ユ帓搴忓苟鎵句腑浣嶆暟
    if len(arr) <= 5:
        sorted_arr = sorted(arr)
        return sorted_arr[len(sorted_arr) // 2]

    medians = []

    # 姣?5 涓厓绱犲垎鎴愪竴缁?
    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        group.sort()

        group_median = group[len(group) // 2]
        medians.append(group_median)

    return median_of_medians(medians)

print(quick_select(arr,4,7,0))
