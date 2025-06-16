n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
visited[0] = 1
cost = 0

for _ in range(n - 1):
    min_edge = float('inf')
    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and g[i][j] > 0 and g[i][j] < min_edge:
                    min_edge = g[i][j]
                    next_node = j
    visited[next_node] = 1
    cost += min_edge

print(cost)

#########################################################

n = int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix (row by row):")
g = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
visited[0] = 1
cost = 0

for _ in range(n - 1):
    min_edge = float('inf')
    next_node = -1
    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and g[i][j] > 0 and g[i][j] < min_edge:
                    min_edge = g[i][j]
                    next_node = j
    if next_node != -1:
        visited[next_node] = 1
        cost += min_edge

print("Minimum cost of spanning tree:", cost)
