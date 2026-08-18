def topsort_recurrsive(adjlist):
    indegree = [0] * len(adjlist)
    order = []

    for v in adjlist:
        for e in adjlist[v]:
            indegree[e] += 1

    def recur():
        srcs = [z for z in range(len(indegree)) if indegree[z] == 0 and z not in order]

        if not srcs:
            return 
        
        for u in srcs:
            order.append(u)
            for e in adjlist[u]:
                indegree[e] -= 1

        recur()

    recur()
    return order

def topsort_Rdfs(adjlist):
    seen = [0] * len(adjlist)
    order = []


    def recur(start):
        seen[start] = 1
        for neib in adjlist[start]:
            if seen[neib] == 0:
                seen[neib] = 1
                recur(neib)

        order.append(start)

    for v in range(len(adjlist)):
        if seen[v] == 0:
            recur(v)

    order.reverse()
    return order

def longest_path(adjlist):
    outd = [-1] * len(adjlist)

        
    return 0




if __name__ == "__main__":
    adj_list = {
        0: [2],
        1: [3, 5, 6],
        2: [4, 5],
        3: [6, 7],
        4: [8],
        5: [8, 9],
        6: [9],
        7: [9, 10],
        8: [],
        9: [],
        10: [],
    }


    print(topsort_Rdfs(adj_list))