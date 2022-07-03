import sys

sys.stdin = open('sample_input.txt')

tests = int(input())

# 전체 집합
A = list(range(1,13))


result = [0]
for _ in range(tests):
    N, K = map(int, input().split())
    count = 0

    # 부분집합 비교 검사 => 2^12개의 부분집합
    for i in range(1<<12):
        total = 0
        elem_count = 0
        for j in range(12):
            if i & (1<<j):
                total += A[j]
                elem_count += 1
        # 부분집합의 원소 갯수가 N이고 합이 K라면
        if elem_count == N and total == K:
            count += 1
    result.append(count)

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))