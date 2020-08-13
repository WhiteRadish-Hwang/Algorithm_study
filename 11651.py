num = int(input())
xy_list = []
for i in range(num):
    pointer = input()
    x,y = pointer.split()
    xy_list.append((int(x),int(y)))
    
def xy_sort(p_list):
    if p_list:
        x_point, y_point = p_list[len(p_list)//2]
        pivot = y_point
        x_pivot = x_point
    else:
        return []

    a_list = []
    b_list = []

    for i in range(len(p_list)):
        x_point, y_point = p_list[i]
        if pivot == y_point:
            if x_pivot > x_point:
                a_list.append(p_list[i])
            elif x_pivot < x_point:
                b_list.append(p_list[i])
        elif pivot > y_point:
            a_list.append(p_list[i])
        else:
            b_list.append(p_list[i])
    return xy_sort(a_list) + [(x_pivot, pivot)] + xy_sort(b_list)

for i in xy_sort(xy_list):
    x, y = i
    print(f"{x} {y}")