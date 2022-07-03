import sys

sys.stdin = open('input.txt')

TEST = int(input())

result = [0]
for _ in range(TEST):
    N = int(input())
    num_list = list(map(int, input().split()))

    if N > 20:
        for i in range(N-1, 0, -1):
            for j in range(i):
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]              

    else:
        # N이 작을 때 선택정렬을 써보자!
        # 오름차순 정렬
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if num_list[min_idx] > num_list[j]:
                    min_idx = j
            num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]
        
    result.append(num_list)

for print_case in range(1, TEST+1):
    print('#{}'.format(print_case),*result[print_case])
    
