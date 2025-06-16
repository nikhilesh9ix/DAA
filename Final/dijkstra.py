import heapq

def shortestReach(n, edges, s):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return [dist[i] if dist[i] != float('inf') else -1 for i in range(1, n + 1) if i != s]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s = int(input())
    print(*shortestReach(n, edges, s))

##########################################################################

import heapq

def shortestReach(n, edges, s):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Because the graph is undirected
    
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]  # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    # Exclude the source node and replace infinity with -1
    return [dist[i] if dist[i] != float('inf') else -1 for i in range(1, n + 1) if i != s]

# Driver code
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n, m = map(int, input("\nEnter number of nodes and edges: ").split())
        print("Enter edges as: u v w")
        edges = [list(map(int, input().split())) for _ in range(m)]
        s = int(input("Enter source node: "))
        result = shortestReach(n, edges, s)
        print("Shortest distances from source:", *result)
