n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

dp = [[0] * (n + 2) for _ in range(n + 2)]

for l in range(1, n + 2):
    for i in range(n + 2 - l):
        j = i + l - 1
        if i == j + 1:
            dp[i][j] = q[i]
        else:
            dp[i][j] = float('inf')
            s = sum(p[i:j+1]) + sum(q[i:j+2])
            for k in range(i, j + 1):
                cost = dp[i][k-1] + dp[k+1][j] + s
                dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])

######################################################

n = int(input("Enter number of keys: "))
p = list(map(float, input("Enter key probabilities (p): ").split()))
q = list(map(float, input("Enter dummy probabilities (q): ").split()))

# dp[i][j]: cost of optimal BST for keys i to j
dp = [[0] * (n + 2) for _ in range(n + 2)]

for l in range(1, n + 2):  # length of the subtree
    for i in range(n + 2 - l):
        j = i + l - 1
        if i == j + 1:
            dp[i][j] = q[i]
        else:
            dp[i][j] = float('inf')
            s = sum(p[i:j+1]) + sum(q[i:j+2])  # total probability weight
            for k in range(i, j + 1):  # try all roots
                cost = dp[i][k - 1] + dp[k + 1][j] + s
                dp[i][j] = min(dp[i][j], cost)

print("Minimum cost of Optimal BST:", dp[0][n - 1])
