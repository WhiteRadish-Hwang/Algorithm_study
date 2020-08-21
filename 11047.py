n, k = list(map(int, input().split()))
coin_list=[]
count = 0
for i in range(n):
    coin_list.append(int(input()))

for i in range(len(coin_list)):
    if k >= coin_list[~i]:
        count += k // coin_list[~i]
        k = k % coin_list[~i]

print(count)