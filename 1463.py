x = int(input())
dp = []

#----------탑다운 방식 >> 재귀제한으로 실패
for i in range(x+1):
    dp.append(-1)
def calculate(ex):
    if ex == 1:
        return 0
    if dp[ex] != -1:
        return dp[ex]
    if ex < 1:
        print(-1)
    result = 100000
    if ex % 3 == 0:
        result = min(result,calculate(ex // 3) + 1)
    if ex % 2 == 0:
        result = min(result,calculate(ex // 2) + 1)
    result = min(result, calculate(ex - 1) + 1)
    dp[ex] = result
    return result

print(calculate(x))


##--------바텀업 방식 시간은 느리나 제한이 없음
# for i in range(x+1):
#     dp.append(1000000)

# dp[1] = 0
# for i in range(1,x):
#     dp[i+1] = min(dp[i+1], dp[i]+1)
#     if i*2 <= x:
#         dp[i*2] = min(dp[i*2],dp[i]+1)
#     if i*3 <= x:
#         dp[i*3] = min(dp[i*3], dp[i]+1)
#     print(dp)
        
# print(dp[x])