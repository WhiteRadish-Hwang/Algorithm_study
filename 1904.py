tiles = int(input())
dp = [-1]*(tiles+1)
# def binary_tiles(n):
#     if n == 1:
#         dp[n] = 1
#         return 1
#     if n == 2:
#         dp[n] = 2
#         return 2
#     if dp[n] != -1:
#         return dp[n]
    
#     dp[n] = binary_tiles(n-2) + binary_tiles(n-1)

#     return dp[n]

# print(binary_tiles(tiles))

if tiles >= 1:
    dp[1] = 1
    if tiles > 1:
        dp[2] = 2

for i in range(3, tiles+1):
    dp[i] = dp[i-2] + dp[i-1]
    dp[i] = dp[i] % 15746
print(dp[tiles])