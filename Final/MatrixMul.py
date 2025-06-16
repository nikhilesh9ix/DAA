n = int(input())
p = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]
for l in range(2, n+1):
    for i in range(n-l+1):
        j = i+l-1
        dp[i][j] = min(dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1] for k in range(i, j))
print(dp[0][n-1])

#####################################################

n = int(input("Enter number of matrices: "))
p = list(map(int, input(f"Enter {n+1} dimensions (for {n} matrices): ").split()))

dp = [[0] * n for _ in range(n)]

# l is the chain length (number of matrices being multiplied)
for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            dp[i][j] = min(dp[i][j], cost)

print("Minimum number of multiplications:", dp[0][n - 1])
