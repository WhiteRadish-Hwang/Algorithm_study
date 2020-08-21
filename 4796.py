lpv_list = []
case = []
idx = 0

while lpv_list == [] or not lpv_list[-1] == [0,0,0]:
    lpv_list.append(list(map(int, input().split())))

for i in range(len(lpv_list)):
    if 1 < lpv_list[i][0] < lpv_list[i][1] < lpv_list[i][2]:
        case.append(0)
        while lpv_list[i][2] >= lpv_list[i][0]:
            lpv_list[i][2] -= lpv_list[i][0]
            case[idx] += lpv_list[i][0]
            if lpv_list[i][2] < lpv_list[i][1] - lpv_list[i][0]:
                lpv_list[i][2] = 0
                break
            else:
                lpv_list[i][2] -= lpv_list[i][1] - lpv_list[i][0]
        case[idx] += lpv_list[i][2]
        idx += 1

for i in range(len(case)):
    print(f"Case {i+1}: {case[i]}")