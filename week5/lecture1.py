def coin_change_b2u(amount,coins):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for x in range(1,amount+1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x],dp[x-c]+1)

    return dp[amount] if dp[amount] < amount+1 else None

import functools

def coin_change_u2b(amount,coins):
    @functools.cache
    def recurrence(amount):

        res = None

        if amount < 0:
            return None
        if amount == 0:
            return 0

        for c in coins:
            n = recurrence(amount - c)
            if n is not None and (res is None or n + 1 < res ):
                res = n + 1

        return res

    return recurrence(amount)




print(coin_change_u2b(5,[1,2,3]))