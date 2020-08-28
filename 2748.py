n = int(input())
dp = [-1]*(n+1)

def fibinachi(n):
    if n == 0:
        dp[n] = 0
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibinachi(n-1) + fibinachi(n-2)
    return dp[n]

print(fibinachi(n))