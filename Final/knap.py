n, c = map(int, input().split())
v = list(map(int, input().split()))
w = list(map(int, input().split()))
dp = [0] * (c + 1)
for i in range(n):
    for j in range(c, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])
print(dp[c])

##########################################################################################

def knapsack(n, c, v, w):
    dp = [0] * (c + 1)
    for i in range(n):
        for j in range(c, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[c]

if __name__ == "__main__":
    n, c = map(int, input("Enter number of items and knapsack capacity: ").split())
    v = list(map(int, input("Enter the values of items: ").split()))
    w = list(map(int, input("Enter the weights of items: ").split()))
    
    result = knapsack(n, c, v, w)
    print("Maximum value that can be carried:", result)