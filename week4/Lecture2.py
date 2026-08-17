from collections import deque
import random

def bfs(adj_list,start):
    seen = [0]*len(adj_list)
    order = []

    queue = deque([start])
    seen[start] = 1

    while queue:
        current = queue.popleft()
        order.append(current)
        for neib in adj_list[current]:
            if not seen[neib]:
                queue.append(neib)
                seen[neib] = 1

    return order

def dfs(adj_list,start_node):
    visited = [0] * len(adj_list)
    order = []
    stack = []

    visited[start_node] = 1
    stack.append(start_node)

    while stack:
        current = stack.pop()
        order.append(current)

        for neib in adj_list[current]:
            if not visited[neib] :
                stack.append(neib)
                visited[neib] = 1

    return order


def dfs_recursive(adj_list,start):
    order = []
    visted = [0]*len(adj_list)

    def dfs_(adj_list,start):

        visted[start] = 1
        order.append(start)

        for neib in adj_list[start]:
            if not visted[neib]:
                dfs_(adj_list,neib)

        return order

    dfs_(adj_list,start)

    return order


def scc(g: list[list[bool]]) -> list[list[int]]:
    seen = [False for _ in g]
    finish_order = []  # list of int vertices

    def dfs(u: int):
        seen[u] = True
        for v in range(len(g)):
            if g[u][v] and not seen[v]:
                dfs(v)
        finish_order.append(u)

    for u in range(len(g)):
        if not seen[u]:
            dfs(u)

    seen = [False for _ in g]

    def dfs2(u: int, sc: list[int]):
        seen[u] = True
        sc.append(u)
        for v in range(len(g)):
            if g[v][u] and not seen[v]:
                dfs2(v, sc)

    sccs = []
    for i in range(len(g) - 1, -1, -1):
        sc = []
        if not seen[finish_order[i]]:
            dfs2(finish_order[i], sc)
            sccs.append(sc)

    return sccs

def dfs_time(adj_list, start):
  visited = [0] * len(adj_list)
  time = []
  timer = 0
  order = []

  def dfs(u):
    nonlocal timer
    visited[u] = 1

    for neib in adj_list[u]:
      if not visited[neib]:
        dfs(neib)


    timer += 1
    time.append((u, timer))
    order.append(u)

  dfs(start)
  return time,order


def transpose_comprehension(matrix: list[list[bool]]) -> list[list[bool]]:
  """Return the transpose of an adjacency matrix."""
  if not matrix or not matrix[0]:
    return []
  rows, cols = len(matrix), len(matrix[0])
  return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

def kosaraju(g: list[list[bool]]) -> list[list[int]]:
    n = len(g)

    # First DFS pass: record vertices by finishing time.
    seen = [False] * n
    finish_order = []

    def dfs1(u: int):
        seen[u] = True
        for v in range(n):
            if g[u][v] and not seen[v]:  # Traverse neighbours from the matrix row.
                dfs1(v)
        finish_order.append(u)

    # Visit every disconnected or previously unreachable vertex.
    for u in range(n):
        if not seen[u]:
            dfs1(u)

    # Build the transpose graph.
    g_t = transpose_comprehension(g)

    # Second DFS pass: collect SCCs from the transpose graph.
    seen = [False] * n  # Reset the visited markers.
    sccs = []

    def dfs2(u: int, sc: list[int]):
        seen[u] = True
        sc.append(u)
        for v in range(n):
            if g_t[u][v] and not seen[v]:  # Follow edges in the transpose graph.
                dfs2(v, sc)

    # Process vertices in descending finishing-time order.
    for i in range(n - 1, -1, -1):
        u = finish_order[i]
        if not seen[u]:
            sc = []
            dfs2(u, sc)
            sccs.append(sc)

    return sccs





def random_graph(n: int, density: float) -> list[list[bool]]:
    g = []
    for i in range(n):
        adj = []
        for j in range(n):
            adj.append(random.random() < density and not i == j)
        g.append(adj)
    return g






if __name__ == "__main__":
    adjList = [
        [1, 5, 2],  # Neighbours of vertex 0
        [5, 0],     # Neighbours of vertex 1
        [5, 0, 4],  # Neighbours of vertex 2
        [1, 4],     # Neighbours of vertex 3
        [0, 2],     # Neighbours of vertex 4
        [1, 0, 2]   # Neighbours of vertex 5
    ]

    start = 1
    _,order = dfs_time(adjList,start)
    print(order)
