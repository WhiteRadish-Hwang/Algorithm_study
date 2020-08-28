n = int(input())
paper = []
zero_count = 0
plus_count = 0
minus_count = 0

for i in range(n):
    paper.append(list(map(int, input().split())))

def paper_cut(idx, jdx, leng):
    global zero_count
    global plus_count
    global minus_count
    check = 0
    for i in range(idx, idx + leng):
        for j in range(jdx,jdx + leng):
            if paper[i][j] != paper[idx][jdx]:
                check += 1
                leng = leng//3
                for r in range(3):
                    for c in range(3):
                        paper_cut(idx+r*leng, jdx+c*leng, leng)
                break
        if check == 1:
            break
    if check != 1:
        if paper[idx][jdx] == 0:
            zero_count += 1
        elif paper[idx][jdx] == 1:
            plus_count += 1
        else:
            minus_count += 1

paper_cut(0, 0, n)
print(minus_count)
print(zero_count)
print(plus_count)