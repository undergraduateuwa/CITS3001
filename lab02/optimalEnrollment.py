import sys


def solve():
    """
    Solves the Optimal Enrolment problem using 0/1 Knapsack Dynamic Programming.
    Maximises expected number of passed units within total available hours H.
    """
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    h = int(tokens[1])

    units = []
    ptr = 2
    for _ in range(n):
        hours = int(tokens[ptr])
        prob = int(tokens[ptr + 1])
        units.append((hours, prob))
        ptr += 2

    # dp[w] stores the maximum percentage sum achievable with effort at most w
    dp = [0] * (h + 1)

    for hours, prob in units:
        for w in range(h, hours - 1, -1):
            candidate = dp[w - hours] + prob
            if candidate > dp[w]:
                dp[w] = candidate

    expected_passes = dp[h] / 100.0
    print(f"{expected_passes:.2f}")


if __name__ == '__main__':
    solve()
