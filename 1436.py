# N = int(input())
# ret_list = []
# num = 666

# while len(ret_list) < N:
#     if '666' in str(num):
#         ret_list.append(num)
#     num += 1

# ret_list = sorted(ret_list)
# print(ret_list[-1])

N = int(input())
cnt = 0
num = 666

while cnt < N:
    if '666' in str(num):
        cnt += 1
    num += 1

print(num-1)