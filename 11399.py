n = int(input())
times = list(map(int, input().split()))
total = 0
plus_num = 0
times = sorted(times)

for i in range(len(times)):
    plus_num += times[i]
    total += plus_num

print(total)