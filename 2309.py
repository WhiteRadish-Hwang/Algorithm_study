height = []
for i in range(9):
    height.append(int(input()))

sum_value = sum(height)
for i in range(len(height)-1):
    for j in range(i+1, len(height)):
        if sum_value - height[i] - height[j] == 100:
            height.pop(j)
            height.pop(i)
            height.sort()
            break
    if 7 == len(height):
        break
for i in height:
    print(i)

# from random import randint

# def quick_sort_part(start,end):
#     pivot = height[end]
#     idx = start
#     for j in range(start, end):
#         if height[j] < pivot:
#             height[j] , height[idx] = height[idx], height[j]
#             idx += 1
#     height[end] , height[idx] = height[idx], height[end]
#     return idx

# def quick_sort(start, end):
#     if start < end:
#         pi = quick_sort_part(start, end)
#         quick_sort(start, pi - 1)
#         quick_sort(pi + 1, end)

# def dwarf_height():
#     stack = 0
#     key_sum = 0
#     history_set = set()
#     idx = 0

#     while key_sum != 100 and stack != 7:
#         i = randint(0, len(height)-1)
#         if stack <= 7 and height[i] not in history_set:
#             history_set.add(height[i])
#             key_sum += height[i]
#             stack += 1
#         if key_sum > 100:
#             key_sum = 0
#             stack = 0
#             history_set.clear()
#     while idx < len(height):
#         if height[idx] not in history_set:
#             height.remove(height[idx])
#             idx = 0
#         else:
#             idx += 1
#     start = 0
#     end = len(height) - 1
#     quick_sort(start, end)

# dwarf_height()
# print(height)


