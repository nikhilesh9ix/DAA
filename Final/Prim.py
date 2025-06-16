import heapq

def prims(n, edges, start):
    g = {i: [] for i in range(1, n+1)}
    for u, v, w in edges:
        g[u].append((w, v))
        g[v].append((w, u))

    vis, heap, cost = set(), [(0, start)], 0
    while len(vis) < n:
        w, u = heapq.heappop(heap)
        if u in vis: continue
        vis.add(u); cost += w
        heap += [(x, v) for x, v in g[u] if v not in vis]
        heapq.heapify(heap)
    return cost

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(prims(n, edges, int(input())))

#############################################

import heapq

def prims(n, edges, start):
    g = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        g[u].append((w, v))
        g[v].append((w, u))

    vis = set()
    heap = [(0, start)]
    cost = 0

    while len(vis) < n:
        w, u = heapq.heappop(heap)
        if u in vis:
            continue
        vis.add(u)
        cost += w
        for wt, v in g[u]:
            if v not in vis:
                heapq.heappush(heap, (wt, v))

    return cost

# Input section
n, m = map(int, input("Enter number of nodes and edges: ").split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start = int(input("Enter the starting node: "))
print("Minimum cost of MST:", prims(n, edges, start))
