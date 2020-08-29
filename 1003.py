t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
cnt0 = 0
cnt1 = 0
def fibonachi(n):
    global cnt0
    global cnt1
    if n == 0:
        dp[n] = 0
        cnt0 += 1
        return dp[n]
    if n == 1:
        dp[n] = 1
        cnt1 += 1
        return dp[n]
    
    if dp[n] != -1:
        cnt0 += dpcnt0[n]
        cnt1 += dpcnt1[n]
        return dp[n]
    dp[n] = fibonachi(n-1) + fibonachi(n-2)
    dpcnt0[n] = cnt0
    dpcnt1[n] = cnt1
    return dp[n]

for i in range(t):
    dp = [-1]*(n[i]+1)
    dpcnt0 = [-1]*(n[i]+1)
    dpcnt1 = [-1]*(n[i]+1)
    fibonachi(n[i])
    print(f"{cnt0} {cnt1}")
    cnt0 = 0
    cnt1 = 0