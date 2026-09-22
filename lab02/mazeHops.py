import sys
from collections import deque


def solve():
    """
    Finds the minimum number of steps to traverse a rectangular maze from 'S' to 'E'
    using Breadth-First Search (BFS).
    """
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    r = int(tokens[0])
    c = int(tokens[1])
    grid = tokens[2:2 + r]

    start = None
    end = None

    for i in range(r):
        for j in range(c):
            ch = grid[i][j]
            if ch == 'S':
                start = (i, j)
            elif ch == 'E':
                end = (i, j)

    if start is None or end is None:
        print(-1)
        return

    if start == end:
        print(0)
        return

    # BFS initialization
    dist = [[-1] * c for _ in range(r)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])

    end_r, end_c = end

    while queue:
        curr_r, curr_c = queue.popleft()
        curr_dist = dist[curr_r][curr_c]

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] != '#' and dist[nr][nc] == -1:
                dist[nr][nc] = curr_dist + 1
                if nr == end_r and nc == end_c:
                    print(curr_dist + 1)
                    return
                queue.append((nr, nc))

    print(-1)


if __name__ == '__main__':
    solve()
