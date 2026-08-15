import random


def partition(arr: list, low: int, high: int) -> int:
    """
    划分函数：选取 arr[high] 作为 pivot，
    将小于 pivot 的元素放到左边，大于等于 pivot 的元素放到右边。
    返回 pivot 最终的索引位置。
    """
    pivot = arr[high]
    i = low - 1  # i 指向小于 pivot 区域的最后一个元素位置

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将 pivot 放到正确的位置（小元素区域的下一个）
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr: list, low: int, high: int) -> int:
    """
    随机化划分：随机选择一个 pivot 并将其换到末尾，然后再执行 partition。
    避免最坏情况 O(n^2) 的发生。
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)


def quickselect(arr: list, low: int, high: int, k: int):
    """
     Quickselect 主函数：
    在 arr[low...high] 中查找第 k 小的元素（1-based 索引，即 k ∈ [1, len(arr)]）。
    """
    # 递归基：如果区间内只有一个元素，直接返回
    if low == high:
        return arr[low]

    # 获取划分后 pivot 的绝对位置 pivot_index
    pivot_index = randomized_partition(arr, low, high)

    # 转化为 1-based 的第 rank 小元素位置
    rank = pivot_index + 1

    if k == rank:
        # 情况 1: 恰好命中目标
        return arr[pivot_index]
    elif k < rank:
        # 情况 2: 目标在左侧，剪枝右侧
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        # 情况 3: 目标在右侧，剪枝左侧
        return quickselect(arr, pivot_index + 1, high, k)


def find_kth_smallest(nums: list, k: int):
    """
    封装函数：对外暴露的易用接口
    """
    if not 1 <= k <= len(nums):
        raise ValueError(f"k 必须在 1 到 {len(nums)} 之间")

    # 拷贝一份原数组，避免修改输入数据
    nums_copy = nums.copy()
    return quickselect(nums_copy, 0, len(nums_copy) - 1, k)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    data = [14, 3, 9, 1, 22, 8, 5]
    print(f"原始数组: {data}")

    # 验证每一个 k (1 到 len(data))
    sorted_data = sorted(data)
    print(f"完整排序后的数组（用于验证）: {sorted_data}\n")

    for k in range(1, len(data) + 1):
        result = find_kth_smallest(data, k)
        print(f"第 {k} 小的元素 (Order Statistic k={k}): {result} (正确答案: {sorted_data[k - 1]})")