n = int(input())

def min_creation():
    cre_param = '1' #생성자
    element_sum = 0 #분해합
    while not cre_param == '1000000' and int(cre_param) < n:
        element_list = list(cre_param)
        element_list = list(map(int, element_list))
        element_sum = sum(element_list) + int(cre_param)
        if element_sum == n:
            return cre_param
        else:
            cre_param = int(cre_param)
            cre_param += 1
            cre_param = str(cre_param)
    return 0
print(min_creation())