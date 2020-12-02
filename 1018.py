NM = list(map(int, input().split()))
board = []
for _ in range(NM[0]):
    board.append(input())
    
for i in range(len(board)):
    board[i] = list(board[i])

result = float('inf')
for box_row in range(len(board) - 7):
    for box_col in range(len(board[box_row]) - 7):
        cnt = 0
        cnt2 = 0
        for row in range(box_row, box_row + 8):
            for col in range(box_col, box_col + 8):
                if (row + col) % 2 == 0:
                    if board[row][col] != 'B': cnt += 1
                    if board[row][col] != 'W': cnt2 += 1
                else:
                    if board[row][col] != 'W': cnt += 1
                    if board[row][col] != 'B': cnt2 += 1
        result = min(result, cnt, cnt2)
print(result)