import sys


def solve():
    """
    Solves the Lab Booking problem (Activity Selection / Interval Scheduling).
    Greedily selects the maximum number of mutually compatible bookings
    by sorting requests by their end times.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    intervals = []
    idx = 1
    for _ in range(n):
        s = int(input_data[idx])
        e = int(input_data[idx + 1])
        intervals.append((s, e))
        idx += 2

    # Sort intervals primarily by end time ascending
    intervals.sort(key=lambda x: x[1])

    count = 0
    # The constraints allow start times of zero, so use an explicit sentinel
    # instead of assuming that every valid start time is greater than -1.
    last_end = None
    for s, e in intervals:
        # A booking that starts exactly when another ends is fine
        if last_end is None or s >= last_end:
            count += 1
            last_end = e

    print(count)


if __name__ == '__main__':
    solve()
