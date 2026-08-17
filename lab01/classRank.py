import sys


sys.setrecursionlimit(200000)


def median_of_medians(arr):
    if len(arr) <= 5:
        arr.sort()
        return arr[len(arr) // 2]

    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    return select_kth(medians, (len(medians) + 1) // 2)


def select_kth(arr, k):
    while True:
        if len(arr) <= 5:
            arr.sort()
            return arr[k - 1]

        pivot = median_of_medians(arr)

        left, middle, right = [], [], []
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        L = len(left)
        M = len(middle)

        if k <= L:
            arr = left
        elif k <= L + M:
            return pivot
        else:
            arr = right
            k -= (L + M)


def main():
    # Read all input tokens.
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    # Keep exactly the first n marks.
    marks = [int(x) for x in input_data[2:2 + n]]

    result = select_kth(marks, k)

    # Flush immediately after printing the result.
    print(result, flush=True)


# Run the command-line entry point.
if __name__ == '__main__':
    main()
