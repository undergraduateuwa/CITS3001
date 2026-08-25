

from functools import cache

def lcs_recursive(s1, s2):
    @cache
    def recur(i, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            res = recur(i - 1, j - 1) + 1
        else:
            res = max(
                recur(i - 1, j),
                recur(i, j - 1)
            )

        return res

    i = len(s1) - 1
    j = len(s2) - 1

    return recur(i, j)

def knapsack_01_recursive(capacity, items_w, items_v):
    @cache
    def recur(item, remaining_capacity):
        # 所有物品都考虑完了
        if item == len(items_w):
            return 0

        # 选择一：不拿当前物品
        skip = recur(item + 1, remaining_capacity)

        # 当前物品放不进去，只能不拿
        if items_w[item] > remaining_capacity:
            return skip

        # 选择二：拿当前物品
        take = (
            items_v[item]
            + recur(
                item + 1,
                remaining_capacity - items_w[item]
            )
        )

        # 返回两种方案中价值更大的
        return max(skip, take)

    return recur(0, capacity)

def knapsack(
    capacity: int,
    items: list[tuple[int, int]]
) -> int:

    rows = len(items) + 1
    cols = capacity + 1

    dpt = [
        [0 for _ in range(cols)]
        for _ in range(rows)
    ]

    for i in range(1, rows):
        wi, vi = items[i - 1]

        for w in range(1, cols):
            if w < wi:
                dpt[i][w] = dpt[i - 1][w]
            else:
                dpt[i][w] = max(
                    dpt[i - 1][w],
                    dpt[i - 1][w - wi] + vi
                )

    return dpt[-1][-1]




if __name__ == '__main__':
    print(lcs_recursive('abc','abc'))