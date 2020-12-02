lines = int(input())
datas = []
for _ in range(lines):
    datas.append(list(map(int, input().split()))) #입력값

def key(a, b):
    return str(a) + ',' + str(b) #key값을 포맷하는 함수

dp = dict()
dp[key(0,0)] = datas[0][0]

for i in range(len(datas)-1):
    for j in range(len(datas[i])):
        if key(i+1,j) in dp:
            maxi = max(dp[key(i+1,j)], dp[key(i,j)] + datas[i+1][j]) #이전데이터와 현재데이터와 비교
            dp[key(i+1,j)] = maxi
        else:
            dp[key(i+1,j)] = dp[key(i,j)] + datas[i+1][j]
        
        if key(i+1,j+1) in dp:
            maxi = max(dp[key(i+1,j+1)], dp[key(i,j)] + datas[i+1][j+1]) #이전데이터와 현재데이터와 비교
            dp[key(i+1,j+1)] = maxi
        else:
            dp[key(i+1,j+1)] = dp[key(i,j)] + datas[i+1][j+1]

max_v = max(dp.values())
print(max_v)