# def partition(list_a, left, right):
#     pivot = list_a[left]
#     i = left
#     j = right

#     while i <= j:
#         while i <= j and list_a[i] <= pivot:
#             i += 1
#         while i <= j and list_a[j] >= pivot:
#             j -= 1
#         if i < j:
#             list_a[i], list_a[j] = list_a[j], list_a[i] # swap
        
#     list_a[left], list_a[j] = list_a[j], list_a[left]
#     return j


# def quick_sort(list_a, left, right):
#     if left < right:
#         s = partition(list_a, left, right)
#         quick_sort(list_a, left, s-1)
#         quick_sort(list_a, s+1, right)


def is_binary_search(a, target, left, right, pre_movemnet=0):
    # pre_movement : 1 (이전 움직인 구간이 왼쪽), 2 (이전 움직인 구간이 오른쪽)
    
    if left > right:
        return False
    
    mid = (left + right) // 2
    
    if target == a[mid]:
        return True

    elif target < a[mid]:
        if pre_movemnet == 1:
            return False
        return is_binary_search(a, target, left, mid-1, 1)

    else:
        if pre_movemnet == 2:
            return False
        return is_binary_search(a, target, mid+1, right, 2)

    

for tc in range(1, int(input())+1):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    # A를 우선 정렬
    A.sort()
    # quick_sort(A, 0, len_A-1) => 런타임 에러
    
    result = 0
    for target in B:
        if is_binary_search(A, target, 0, len_A-1):
            result += 1

    print('#{} {}'.format(tc, result))
    

        
