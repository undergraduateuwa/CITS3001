import sys
from collections import deque

sys.setrecursionlimit(200000)


def zero_one_bfs(start: int, target: int, n: int, adj: list[list[tuple[int, int]]]) -> int:
    """
    Computes shortest path from start to target in a directed graph where
    edge weights are in {0, 1} using 0-1 BFS.
    """
    if start == target:
        return 0

    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([(0, start)])

    while dq:
        d, u = dq.popleft()

        if d > dist[u]:
            continue

        if u == target:
            return d

        for v, w in adj[u]:
            new_d = d + w
            if new_d < dist[v]:
                dist[v] = new_d
                if w == 0:
                    dq.appendleft((new_d, v))
                else:
                    dq.append((new_d, v))

    # The statement guarantees connectivity after ignoring directions, but
    # keeping the unreachable case explicit makes this helper safe to reuse.
    return -1 if dist[target] == float('inf') else int(dist[target])


def solve():
    """
    Computes the minimum demerit points for Travis to drive from O to D and back from D to O.
    Traversing a one-way road in its legal direction incurs 0 demerits.
    Traversing a one-way road in the reverse direction incurs 1 demerit.
    The two legs are independent, so we run two 0-1 BFS traversals.
    """
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    origin = int(tokens[1])
    destination = int(tokens[2])

    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    ptr = 3
    for u in range(n):
        k = int(tokens[ptr])
        ptr += 1
        for _ in range(k):
            v = int(tokens[ptr])
            ptr += 1
            # Driving u -> v in the legal direction costs 0
            adj[u].append((v, 0))
            # Driving v -> u in the reverse direction costs 1
            adj[v].append((u, 1))

    # Leg 1: Origin -> Destination
    cost_o_to_d = zero_one_bfs(origin, destination, n, adj)
    # Leg 2: Destination -> Origin
    cost_d_to_o = zero_one_bfs(destination, origin, n, adj)

    if cost_o_to_d == -1 or cost_d_to_o == -1:
        print(-1)
    else:
        print(cost_o_to_d + cost_d_to_o)


if __name__ == '__main__':
    solve()
