n = int(input())
scores = list(map(int, input().split()))

def part_arr(start, end):
    pivot = (start+end) // 2
    i = pivot
    j = pivot
    arr_sum = scores[pivot]
    minimum = scores[pivot]
    if start == end:
        return scores[start] ** 2
    if start + 1 == end:
        return max(part_arr(start, start), part_arr(end,end))

    maximum = max(part_arr(start, pivot-1), part_arr(pivot, end))
    
    while i > start or j < end:
        if i > start and j < end and scores[i-1] > scores[j+1]:
            i -= 1
            arr_sum += scores[i]
            if minimum > scores[i]:
                minimum = scores[i]
        else:
            if j < end:
                j += 1
                arr_sum += scores[j]
                if minimum > scores[j]:
                    minimum = scores[j]
            else:
                i -= 1
                arr_sum += scores[i]
                if minimum > scores[i]:
                    minimum = scores[i]
        result = arr_sum * minimum

        maximum = max(maximum, result)
    return maximum
print(part_arr(0, n-1))