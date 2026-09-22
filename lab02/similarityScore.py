import sys


def solve():
    """
    Computes the length of the Longest Common Subsequence (LCS) between two strings
    using dynamic programming with O(min(len1, len2)) space.
    """
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    s1 = tokens[0]
    s2 = tokens[1]

    # Ensure s2 is the shorter string to minimize space
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    n = len(s2)
    dp = [0] * (n + 1)

    for c1 in s1:
        prev = 0
        for j, c2 in enumerate(s2):
            tmp = dp[j + 1]
            if c1 == c2:
                dp[j + 1] = prev + 1
            elif dp[j] > dp[j + 1]:
                dp[j + 1] = dp[j]
            prev = tmp

    print(dp[n])


if __name__ == '__main__':
    solve()
