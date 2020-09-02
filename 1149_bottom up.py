n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

dp = dict()

def key(row, col):
    return str(row) + ":" + str(col)

for j in range(3):
    dp[key(0, j)] = cost[0][j]
for row in range(1, n):
        dp[key(row, 0)] = cost[row][0] + min(dp[key(row-1, 1)], dp[key(row-1, 2)])

        dp[key(row, 1)] = cost[row][1] + min(dp[key(row-1, 0)], dp[key(row-1, 2)])

        dp[key(row, 2)] = cost[row][2] + min(dp[key(row-1, 0)], dp[key(row-1, 1)])
print(min(dp[key(row,0)], dp[key(row,1)], dp[key(row,2)]))