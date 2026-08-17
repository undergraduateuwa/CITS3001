from collections import deque
import random

# Visit reachable vertices in breadth-first order.
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

# Visit reachable vertices with depth-first search.
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


# Visit reachable vertices recursively in depth-first order.
def dfs_recursive(adj_list,start):
    order = []
    visted = [0]*len(adj_list)

    # Visit vertices recursively in depth-first order.
    def dfs_(adj_list,start):

        visted[start] = 1
        order.append(start)

        for neib in adj_list[start]:
            if not visted[neib]:
                dfs_(adj_list,neib)

        return order

    dfs_(adj_list,start)

    return order


# Return strongly connected components using Kosaraju's method.
def scc(g: list[list[bool]]) -> list[list[int]]:
    seen = [False for _ in g]
    finish_order = []  # list of int vertices

    # Visit reachable vertices with depth-first search.
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

    # Collect one strongly connected component.
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

# Return DFS finishing times and visit order.
def dfs_time(adj_list, start):
  visited = [0] * len(adj_list)
  time = []
  timer = 0
  order = []

  # Visit reachable vertices with depth-first search.
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


# Return the transpose of a Boolean adjacency matrix.
def transpose_comprehension(matrix: list[list[bool]]) -> list[list[bool]]:
  """閭绘帴鐭╅樀杞疆"""
  if not matrix or not matrix[0]:
    return []
  rows, cols = len(matrix), len(matrix[0])
  return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

# Find strongly connected components with two DFS passes.
def kosaraju(g: list[list[bool]]) -> list[list[int]]:
    n = len(g)

    # ================= 1. 绗竴閬?DFS锛氳褰曞畬鎴愭椂闂?=================
    seen = [False] * n
    finish_order = []

    # Run the first DFS pass and record finishing order.
    def dfs1(u: int):
        seen[u] = True
        for v in range(n):
            if g[u][v] and not seen[v]:  # 鐭╅樀鏂瑰紡閬嶅巻閭诲眳
                dfs1(v)
        finish_order.append(u)

    # 寰幆纭繚璁块棶鍒版墍鏈夊绔?鏈埌杈剧殑鑺傜偣
    for u in range(n):
        if not seen[u]:
            dfs1(u)

    # ================= 2. 鑾峰彇鍙嶅悜鍥?=================
    g_t = transpose_comprehension(g)

    # ================= 3. 绗簩閬?DFS锛氬湪鍙嶅悜鍥句笂鏀堕泦 SCC =================
    seen = [False] * n  # 閲嶇疆璁块棶鏍囪
    sccs = []

    # Collect one strongly connected component.
    def dfs2(u: int, sc: list[int]):
        seen[u] = True
        sc.append(u)
        for v in range(n):
            if g_t[u][v] and not seen[v]:  # 娌跨潃鍙嶅悜鍥剧殑杈归亶鍘?
                dfs2(v, sc)

    # 鎸夌収瀹屾垚鏃堕棿浠庡ぇ鍒板皬锛堥€嗗簭锛夐亶鍘?
    for i in range(n - 1, -1, -1):
        u = finish_order[i]
        if not seen[u]:
            sc = []
            dfs2(u, sc)
            sccs.append(sc)

    return sccs





# Generate a directed graph as a Boolean adjacency matrix.
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
        [1, 5, 2],  # 鑺傜偣 0 鐨勯偦灞?
        [5, 0],     # 鑺傜偣 1 鐨勯偦灞?
        [5, 0, 4],  # 鑺傜偣 2 鐨勯偦灞?
        [1, 4],     # 鑺傜偣 3 鐨勯偦灞?
        [0, 2],     # 鑺傜偣 4 鐨勯偦灞?
        [1, 0, 2]   # 鑺傜偣 5 鐨勯偦灞?
    ]

    start = 1
    _,order = dfs_time(adjList,start)
    print(order)
