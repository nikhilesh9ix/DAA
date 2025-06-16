def dfs(g, v, visited, count, n):
    if count == n:
        return True
    for u in g[v]:
        if not visited[u]:
            visited[u] = True
            if dfs(g, u, visited, count + 1, n):
                return True
            visited[u] = False
    return False

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

for i in range(n):
    visited = [False] * n
    visited[i] = True
    if dfs(g, i, visited, 1, n):
        print("YES")
        exit()
print("NO")


#################################################

def dfs(graph, current, visited, count, n):
    if count == n:
        return True
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            if dfs(graph, neighbor, visited, count + 1, n):
                return True
            visited[neighbor] = False  # Backtrack
    return False

# Input section
n, m = map(int, input("Enter number of nodes and edges: ").split())
graph = [[] for _ in range(n)]

print("Enter edges (0-based index):")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Try starting DFS from every node
for i in range(n):
    visited = [False] * n
    visited[i] = True
    if dfs(graph, i, visited, 1, n):
        print("YES")
        break
else:
    print("NO")
