NM = list(map(int, input().split()))
num = list(map(int, input().split()))
cnt = NM[0]
aim = NM[1]
closer = float('-inf')

def BlackJack(cnt, aim, closer):
    for i in range(cnt):
        for j in range(i+1, cnt):
            for k in range(j+1, cnt):
                score = num[i] + num[j] + num[k]
                if score <= aim:
                    closer = max(closer, score)
    print(closer)

BlackJack(cnt, aim, closer)