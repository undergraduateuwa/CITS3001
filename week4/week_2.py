from collections import deque
def bfs(adj_list, start_node):
    """
    使用 deque 实现图的广度优先搜索 (BFS)
    
    :param adj_list: 图的邻接表 (List[List[int]])
    :param start_node: 起始节点索引
    :return: 节点的遍历顺序 (List[int])
    """
    # 记录节点是否被访问过，避免重复访问
    visited = [False] * len(adj_list)
    order = []
    
    # 使用 deque 创建队列，并将起始节点放入队列
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        # 1. 从队首弹出当前节点
        current = queue.popleft()
        order.append(current)
        
        # 2. 遍历当前节点的所有邻居
        for neighbor in adj_list[current]:
            # 3. 如果邻居未被访问，则标记为已访问并加入队列尾部
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
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

    def dfs_(adj_list,start,order,visted):

        visted[start] = 1
        order.append(start)

        for neib in adj_list[start]:
            if not visted[neib]:
                dfs_(adj_list,neib,order,visted)

        return order

    dfs_(adj_list,start,order,visted)

    return order
    
    

def bfs_time(adj_list,start):
    order = []
    visted = [0]*len(adj_list)
    time = []
    timer = 0

    def dfs_(adj_list,start,order,visted):

        visted[start] = 1
        order.append(start)
        for neib in adj_list[start]:
            if not visted[neib]:
                dfs_(adj_list,neib,order,visted)

        return order

    dfs_(adj_list,start,order,visted)

    return order

# def scc(g:list[list[bool]])->list[list[int]]:
#     seen =

def Kosaraju(adjlist):

    return 0


if __name__ == "__main__":
    # 使用之前图中的邻接表数据
    adjList = [
        [1, 5, 2],  # 节点 0 的邻居
        [5, 0],     # 节点 1 的邻居
        [5, 0, 4],  # 节点 2 的邻居
        [1, 4],     # 节点 3 的邻居
        [0, 2],     # 节点 4 的邻居
        [1, 0, 2]   # 节点 5 的邻居
    ]
    
    start = 1
    traversal_order = dfs_recursive(adjList, start)
    print(f"从节点 {start} 开始的 BFS 遍历顺序: {traversal_order}") 