# Created on iPad.
arr = [711,170,343,7,452,617,144,417]
def buck_sort(arr):
    res = 0
    return result



def radix_sort(arr):
    if not arr:
        return arr

    # Find the largest value to determine how many digit passes are needed.
    max_num = max(arr)

    # exp identifies the digit position processed in the current pass.
    # exp = 1: ones place
    # exp = 10: tens place
    # exp = 100: hundreds place
    exp = 1

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp):
    n = len(arr)

    # Store the result of this counting-sort pass.
    output = [0] * n

    # Count occurrences for the ten possible digits, 0 through 9.
    count = [0] * 10

    # Count each digit at the current position.
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Convert frequencies into cumulative positions.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Traverse right to left so the sorting pass remains stable.
    for i in range(n - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % 10

        output[count[digit] - 1] = num
        count[digit] -= 1

    # Copy the sorted result back into the original list.
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

    # Choose a pivot that guarantees a sufficiently balanced split.
    pivot_value = median_of_medians(current)

    # Locate the chosen pivot within the current slice.
    pivot_index = arr.index(pivot_value, lower, upper + 1)

    # Move the pivot to the end before partitioning.
    arr[pivot_index], arr[upper] = arr[upper], arr[pivot_index]

    i = lower - 1

    for j in range(lower, upper):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[upper] = arr[upper], arr[i + 1]

    return i + 1

def median_of_medians(arr):
    # Base case: sort groups of at most five and return their median.
    if len(arr) <= 5:
        sorted_arr = sorted(arr)
        return sorted_arr[len(sorted_arr) // 2]

    medians = []

    # Divide the values into groups of five.
    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        group.sort()

        group_median = group[len(group) // 2]
        medians.append(group_median)

    return median_of_medians(medians)

print(quick_select(arr,4,7,0))
