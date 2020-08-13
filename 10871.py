# from random import shuffle

# N, X = map(int, input().split())
# a_list = []

# for i in range(1, N+1):
#     a_list.append(i)
#     i += 1
# shuffle(a_list)

# def smaller_than_N(i_list, comparer):

#     for i in range(len(i_list)):
#         if comparer > i_list[i]:
#             print(i_list[i], end=" ")

# smaller_than_N(a_list, X)

N, X = map(int, input().split())
a_list = list(map(int,input().split()))
print(a_list)
def smaller_than_N(i_list, comparer):
    for i in range(len(i_list)):
        if comparer > i_list[i]:
            print(i_list[i], end=" ")

smaller_than_N(a_list, X)