
def partition(list_a, left, right):
    pivot = list_a[left]
    i = left
    j = right

    while i <= j:
        while i <= j and list_a[i] <= pivot:
            i += 1
        while i <= j and list_a[j] >= pivot:
            j -= 1
        if i < j:
            list_a[i], list_a[j] = list_a[j], list_a[i] # swap
        
    list_a[left], list_a[j] = list_a[j], list_a[left]
    return j


def quick_sort(list_a, left, right):
    if left < right:
        s = partition(list_a, left, right)
        quick_sort(list_a, left, s-1)
        quick_sort(list_a, s+1, right)




for tc in range(1, int(input())+1):
    N = int(input())

    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N-1)
    print('#{} {}'.format(tc, numbers[N//2]))


