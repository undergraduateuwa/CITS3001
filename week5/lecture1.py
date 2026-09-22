# Find the minimum coin count with bottom-up dynamic programming.
def coin_change_b2u(amount,coins):
    # Total time complexity: O(amount * len(coins)).
    # Total space complexity: O(amount) for the dp list.
    # dp[x] stores the minimum number of coins needed to make amount x.
    # amount + 1 is used as "infinity": an amount can never need more
    # than amount coins (worst case, all 1-value coins), so any value
    # left at amount + 1 is unreachable.
    dp = [amount+1] * (amount+1)
    # List construction is O(amount); the base case assignment is O(1).
    dp[0] = 0

    # Outer loop: amount iterations; inner loop: len(coins) iterations.
    # This block is O(amount * len(coins)). The body only does O(1) work
    # (one comparison and one min), so the nested loops dominate runtime.
    for x in range(1,amount+1):
        for c in coins:
            if c <= x:
                # Recurrence: dp[x] = min(dp[x], dp[x - c] + 1) per coin c.
                dp[x] = min(dp[x],dp[x-c]+1)

    # O(1) lookup: return the answer, or None if dp[amount] stayed at
    # the "infinity" value (the amount cannot be formed).
    return dp[amount] if dp[amount] < amount+1 else None

import functools

# Find the minimum coin count with cached recursion.
def coin_change_u2b(amount,coins):
    # Total time complexity: O(amount * len(coins)).
    # Only amount + 1 distinct subproblems exist (amounts 0..amount), and
    # functools.cache guarantees each subproblem is solved at most once.
    # Each subproblem scans all len(coins) coins, giving the product.
    # Total space complexity: O(amount) cache entries plus O(amount)
    # recursion depth (each call decreases the amount by at least 1).
    @functools.cache
    # Solve the remaining coin-change subproblem recursively.
    def recurrence(amount):

        # res holds the best (fewest-coin) count found so far; None means
        # no valid continuation has been found yet. O(1) to initialize.
        res = None

        # Base cases, O(1) each:
        # negative amounts cannot be formed; amount 0 needs no coins.
        if amount < 0:
            return None
        if amount == 0:
            return 0

        # Try every coin as the last coin used: O(len(coins)) per
        # subproblem. Because of functools.cache, this loop runs once per
        # distinct amount in 0..amount, so the total across the whole
        # call tree is O(amount * len(coins)).
        for c in coins:
            n = recurrence(amount - c)
            # Keep the smallest candidate: n coins for amount - c plus the
            # coin c itself. O(1) per coin.
            if n is not None and (res is None or n + 1 < res ):
                res = n + 1

        # O(1): return the best count found, or None if this amount
        # cannot be formed at all.
        return res

    # O(1) to invoke; this single call triggers the O(amount * len(coins))
    # cached computation above.
    return recurrence(amount)


# Example run: minimum coins to make 5 with [1, 2, 3] is 2 (e.g. 2 + 3).
print(coin_change_u2b(5,[1,2,3]))
