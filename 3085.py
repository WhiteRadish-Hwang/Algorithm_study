n = int(input())
candies = []
maximum = 0
result = 0

for i in range(n):
    candies.append(input())
    candies[i] = list(candies[i])

def count_same_candies(target_list, aidx, bidx):
    count = 0
    direct = 0
    max_count = 0
    while direct < 4:
        try:
            if target_list[aidx][bidx] == target_list[aidx][bidx-1] and direct == 0:
                if bidx-1 < 0:
                    raise IndexError
                bidx -= 1
                count += 1
            elif target_list[aidx][bidx] == target_list[aidx][bidx+1] and direct == 1:
                bidx += 1
                count += 1
            elif target_list[aidx][bidx] == target_list[aidx-1][bidx] and direct == 2:
                if aidx-1 < 0:
                    raise IndexError
                aidx -= 1
                count += 1
            elif target_list[aidx][bidx] == target_list[aidx+1][bidx] and direct == 3:
                aidx += 1
                count += 1
            else:
                direct += 1
                if max_count < count:
                    max_count = count
                count = 0
        except IndexError:
            if max_count < count:
                max_count = count
            count = 0
            direct += 1
    return max_count

for i in range(len(candies)): #가로의 경우의 수
    for j in range(1, len(candies[i])):
        candies[i][j], candies[i][j-1] = candies[i][j-1], candies[i][j]
        result = count_same_candies(candies, i, j)
        if maximum < result:
            maximum = result
        result = count_same_candies(candies, i, j-1)
        if maximum < result:
            maximum = result
        candies[i][j], candies[i][j-1] = candies[i][j-1], candies[i][j]

for i in range(1, len(candies)): # 세로의 경우의 수
    for j in range(len(candies[i])):
        candies[i][j], candies[i-1][j] = candies[i-1][j], candies[i][j]
        result = count_same_candies(candies, i, j)
        if maximum < result:
            maximum = result
        result = count_same_candies(candies, i-1, j)
        if maximum < result:
            maximum = result
        candies[i][j], candies[i-1][j] = candies[i-1][j], candies[i][j]

print(maximum+1)