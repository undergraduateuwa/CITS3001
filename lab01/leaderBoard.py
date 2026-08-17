import sys
import heapq


# Print the k-th fastest time after each finisher.
def process_fun_run_times():
    """
    Reads inputs from standard input and prints the k-th fastest
    chip time dynamically after each finisher.
    """
    # Read all tokens from standard input for fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    times = [int(x) for x in input_data[2:2 + n]]

    # Max-heap to store the k smallest running times seen so far.
    # Note: Python's heapq is a min-heap by default.
    # We negate numbers (-val) to turn it into a max-heap.
    max_heap = []

    output_lines = []

    for t in times:
        # Push the current runner's time (negated) into the max-heap
        heapq.heappush(max_heap, -t)

        # If the heap size exceeds k, remove the largest element seen so far
        if len(max_heap) > k:
            heapq.heappop(max_heap)

        # Output result based on current number of elements in heap
        if len(max_heap) < k:
            output_lines.append("-1")
        else:
            # The root (-max_heap[0]) is the maximum among the k smallest elements,
            # which is precisely the k-th smallest element.
            output_lines.append(str(-max_heap[0]))

    # Print all results separated by newlines
    sys.stdout.write("\n".join(output_lines) + "\n")


if __name__ == '__main__':
    process_fun_run_times()
