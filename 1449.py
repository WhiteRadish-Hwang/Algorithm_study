n, l = list(map(int, input().split()))
n_list = list(map(int,input().split()))
count = 0
idx = 0
start = 0
n_list.sort()
while idx <= len(n_list)-1:
    for j in range(l):
        if idx < len(n_list)-1 and l + n_list[start] - 0.5 >= n_list[idx+1] + 0.5:
            idx += 1
        else:
            start = idx + 1
            idx += 1
            break
    count += 1
print(count)