

def merge(left, right):
    global cnt


    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt += 1
    if left[-1] > right[-1]:
        cnt += 1
    
    left_idx = 0
    right_idx = 0
    temp = []
    while left_idx < len(left) or right_idx < len(right):
        # print('left_idx', left_idx, 'right_idx', right_idx)
        if left_idx == len(left) and right_idx < len(right):
            temp.append(right[right_idx])
            right_idx += 1
            continue
        
        elif right_idx == len(right) and left_idx < len(left):
            temp.append(left[left_idx])
            left_idx += 1
            continue

        if left[left_idx] <= right[right_idx]:
            temp.append(left[left_idx])
            left_idx += 1

        else:
            temp.append(right[right_idx])
            right_idx += 1
    return temp

def merge_sort(list_a):
    if len(list_a) == 1:
        return list_a
    
    middle = len(list_a) // 2
    
    
    left = merge_sort(list_a[:middle]) 
    right = merge_sort(list_a[middle:])

    return merge(left, right)


for tc in range(1, int(input())+1):
    N = int(input())

    numbers = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(numbers)[len(numbers)//2]
    
    print('#{} {} {}'.format(tc, result, cnt))

