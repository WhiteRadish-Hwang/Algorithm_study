n = int(input())
height = []
for i in range(n):
    height.append(int(input()))

def histogram(start, end):
    pivot = (end + start) // 2
    left = pivot
    right = pivot
    hei = height[pivot]

    if start == end:
        return height[start]
    if start + 1 == end:
        lower_height = min(height[start],height[end])
        highest_height = max(height[start],height[end])
        return max(lower_height * 2, highest_height) #경우의 수를 더 다양하게 볼 필요가 있음
    
    max_value = max(histogram(start, pivot-1), histogram(pivot,end))

    while right < end or start < left: #while의 범위를 정확하게 변수없이 정하는게 중요
        if left-1 >= start:
            left_height = min(height[left],height[left-1])
        if right+1 <= end:
            right_height = min(height[right], height[right+1])
        
        if left > start and left_height > right_height:
            hei = min(hei,left_height)
            left -= 1
        else: #elif가 아닌 하위 if문을 이용해서 인덱스를 제한하는것이 더 깔끔하고 정확함
            hei = min(hei, right_height)
            if right < end:
                right += 1
            else:
                left -= 1
                hei = min(hei, left_height)

        width = right - left + 1 #width 식을 +1이 아닌 인덱스처럼 생각했어야함.
        max_value = max(max_value, width*hei)

    return max_value

print(histogram(0, n-1))