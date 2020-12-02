N = int(input())
mass = []
for _ in range(N):
    mass.append(list(map(int, input().split())))
start = 0
result = []
for _ in range(len(mass)):
    cnt = 0
    person = mass[start]
    for p in range(len(mass)):
        if p == start:
            continue
        if person[0] < mass[p][0]:
            if person[1] < mass[p][1]:
                cnt += 1
    result.append(cnt + 1)
    start += 1

for i in result:
    print(i, end=" ")