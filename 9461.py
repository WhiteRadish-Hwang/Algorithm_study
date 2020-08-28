test_case = int(input())
n = []
for i in range(test_case):
    n.append(int(input()))

def padoban(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 1
    if dp[k] != -1:
        return dp[k]
    dp[k] = padoban(k-3) + padoban(k-2)
    return dp[k]

for i in range(test_case):
    dp = [-1] * (n[i]+1)
    print(padoban(n[i]))