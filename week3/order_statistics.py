import random


def partition(arr: list, low: int, high: int) -> int:
    """Partition around arr[high] and return the pivot's final index.

    Values smaller than the pivot move left; values greater than or equal to
    the pivot remain on the right.
    """
    pivot = arr[high]
    i = low - 1  # Track the end of the region containing smaller values.

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot immediately after the region of smaller values.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr: list, low: int, high: int) -> int:
    """Choose a random pivot, move it to the end, and partition the slice.

    Randomization reduces the chance of repeatedly encountering O(n^2)
    partitions.
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)


def quickselect(arr: list, low: int, high: int, k: int):
    """Find the one-based k-th smallest value in arr[low:high + 1]."""
    # Base case: a one-element slice contains the requested value.
    if low == high:
        return arr[low]

    # Get the pivot's absolute index after partitioning.
    pivot_index = randomized_partition(arr, low, high)

    # Convert the pivot index to a one-based rank.
    rank = pivot_index + 1

    if k == rank:
        # The pivot has exactly the requested rank.
        return arr[pivot_index]
    elif k < rank:
        # Search the left partition and discard the right partition.
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        # Search the right partition and discard the left partition.
        return quickselect(arr, pivot_index + 1, high, k)


def find_kth_smallest(nums: list, k: int):
    """Return the k-th smallest value without modifying the input list."""
    if not 1 <= k <= len(nums):
        raise ValueError(f"k 必须在 1 到 {len(nums)} 之间")

    # Work on a copy so the caller's list is unchanged.
    nums_copy = nums.copy()
    return quickselect(nums_copy, 0, len(nums_copy) - 1, k)


# Demonstration and verification code.
if __name__ == "__main__":
    data = [14, 3, 9, 1, 22, 8, 5]
    print(f"原始数组: {data}")

    # Verify every valid rank from 1 through len(data).
    sorted_data = sorted(data)
    print(f"完整排序后的数组（用于验证）: {sorted_data}\n")

    for k in range(1, len(data) + 1):
        result = find_kth_smallest(data, k)
        print(f"第 {k} 小的元素 (Order Statistic k={k}): {result} (正确答案: {sorted_data[k - 1]})")
