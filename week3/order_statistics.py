import random


# Partition a slice and return the pivot position.
def partition(arr: list, low: int, high: int) -> int:
    """
    鍒掑垎鍑芥暟锛氶€夊彇 arr[high] 浣滀负 pivot锛?
    灏嗗皬浜?pivot 鐨勫厓绱犳斁鍒板乏杈癸紝澶т簬绛変簬 pivot 鐨勫厓绱犳斁鍒板彸杈广€?
    杩斿洖 pivot 鏈€缁堢殑绱㈠紩浣嶇疆銆?
    """
    pivot = arr[high]
    i = low - 1  # i 鎸囧悜灏忎簬 pivot 鍖哄煙鐨勬渶鍚庝竴涓厓绱犱綅缃?

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 灏?pivot 鏀惧埌姝ｇ‘鐨勪綅缃紙灏忓厓绱犲尯鍩熺殑涓嬩竴涓級
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Choose a random pivot and partition the slice.
def randomized_partition(arr: list, low: int, high: int) -> int:
    """
    闅忔満鍖栧垝鍒嗭細闅忔満閫夋嫨涓€涓?pivot 骞跺皢鍏舵崲鍒版湯灏撅紝鐒跺悗鍐嶆墽琛?partition銆?
    閬垮厤鏈€鍧忔儏鍐?O(n^2) 鐨勫彂鐢熴€?
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)


# Return the one-based k-th smallest value.
def quickselect(arr: list, low: int, high: int, k: int):
    """
     Quickselect 涓诲嚱鏁帮細
    鍦?arr[low...high] 涓煡鎵剧 k 灏忕殑鍏冪礌锛?-based 绱㈠紩锛屽嵆 k 鈭?[1, len(arr)]锛夈€?
    """
    # 閫掑綊鍩猴細濡傛灉鍖洪棿鍐呭彧鏈変竴涓厓绱狅紝鐩存帴杩斿洖
    if low == high:
        return arr[low]

    # 鑾峰彇鍒掑垎鍚?pivot 鐨勭粷瀵逛綅缃?pivot_index
    pivot_index = randomized_partition(arr, low, high)

    # 杞寲涓?1-based 鐨勭 rank 灏忓厓绱犱綅缃?
    rank = pivot_index + 1

    if k == rank:
        # 鎯呭喌 1: 鎭板ソ鍛戒腑鐩爣
        return arr[pivot_index]
    elif k < rank:
        # 鎯呭喌 2: 鐩爣鍦ㄥ乏渚э紝鍓灊鍙充晶
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        # 鎯呭喌 3: 鐩爣鍦ㄥ彸渚э紝鍓灊宸︿晶
        return quickselect(arr, pivot_index + 1, high, k)


# Return the k-th smallest value without changing the input list.
def find_kth_smallest(nums: list, k: int):
    """
    灏佽鍑芥暟锛氬澶栨毚闇茬殑鏄撶敤鎺ュ彛
    """
    if not 1 <= k <= len(nums):
        raise ValueError(f"k 蹇呴』鍦?1 鍒?{len(nums)} 涔嬮棿")

    # 鎷疯礉涓€浠藉師鏁扮粍锛岄伩鍏嶄慨鏀硅緭鍏ユ暟鎹?
    nums_copy = nums.copy()
    return quickselect(nums_copy, 0, len(nums_copy) - 1, k)


# ==================== 娴嬭瘯浠ｇ爜 ====================
if __name__ == "__main__":
    data = [14, 3, 9, 1, 22, 8, 5]
    print(f"鍘熷鏁扮粍: {data}")

    # 楠岃瘉姣忎竴涓?k (1 鍒?len(data))
    sorted_data = sorted(data)
    print(f"瀹屾暣鎺掑簭鍚庣殑鏁扮粍锛堢敤浜庨獙璇侊級: {sorted_data}\n")

    for k in range(1, len(data) + 1):
        result = find_kth_smallest(data, k)
        print(f"绗?{k} 灏忕殑鍏冪礌 (Order Statistic k={k}): {result} (姝ｇ‘绛旀: {sorted_data[k - 1]})")
