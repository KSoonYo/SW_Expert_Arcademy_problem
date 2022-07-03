import sys

sys.stdin = open('sample_input.txt')

tests = int(input())

result = [0]

# k번째로 큰 수 찾기 (1부터 시작)
def max_select(num_list, k):
    num = num_list[:]
    for i in range(0, k):
        max_index = i
        for j in range(i+1, len(num)):
            if num[max_index] < num[j]:
                max_index = j
        num[i], num[max_index] = num[max_index], num[i]
    return num[k-1]

# k번째로 작은 수 찾기 (1부터 시작)
def min_select(num_list, k):
    num = num_list[:]
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num[k-1]


result = [0]
for _ in range(tests):
    # 정수 개수
    N = int(input())

    # 숫자 리스트
    num = list(map(int, input().split()))

    # n번째 큰 수와 작은 수를 각 자리에 맞게 배치
    # 순서는 큰 수 -> 작은 수 -> 큰 수 .... 
    # 짝수 번째 일 때는 큰 수, 홀수 번째 일 때는 작은 수

    max_idx_cnt = 1
    min_idx_cnt = 1
    copied_list = num[:]
    for idx in range(N):
        # 홀수 번째 idx -> k번째로 작은 수 
        if idx % 2:
            num[idx] = min_select(copied_list, min_idx_cnt)
            min_idx_cnt += 1

        # 짝수 번째 idx -> k번째로 큰 수
        else:
            num[idx] = max_select(copied_list, max_idx_cnt)
            max_idx_cnt += 1
    if len(num) > 10:
        result.append(num[:10])
    else:
        result.append(num[:10])

for print_case in range(1, tests+1):
    print('#{}'.format(print_case), *result[print_case])