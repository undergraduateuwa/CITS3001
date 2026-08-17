import sys


sys.setrecursionlimit(200000)


# Select a robust pivot with the median-of-medians method.
def median_of_medians(arr):
    if len(arr) <= 5:
        arr.sort()
        return arr[len(arr) // 2]

    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    return select_kth(medians, (len(medians) + 1) // 2)


# Return the one-based k-th smallest value.
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


# Read input and print the requested result.
def main():
    # 璇诲彇鍏ㄩ儴杈撳叆鏁版嵁
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    # 鎴彇 n 涓暟鎹?
    marks = [int(x) for x in input_data[2:2 + n]]

    result = select_kth(marks, k)

    # 纭繚鐩存帴鎵撳嚭骞?flush 缂撳啿鍖?
    print(result, flush=True)


# 蹇呴』纭繚姝ゅ叆鍙ｅ瓨鍦紒
if __name__ == '__main__':
    main()
