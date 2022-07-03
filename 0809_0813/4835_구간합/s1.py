import sys

sys.stdin = open('input.txt')

tests = int(input())

result = [0]

for _ in range(tests):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_sum = 0 # 정수가 모두 양수이므로 0을 최저로 둘 수 있음

    # 요소 + 구간 안에 있는 요소들을 모두 더하고
    # min_sum과 max_sum 업데이트
    # idx 0이라면 min_sum은 가장 먼저 더해진 숫자합
    # 요소 + 구간이 n을 넘으면 즉시 종료
    for idx in range(n):
        if idx + m > n:
            break
        else:
            # 부분 요소합 초기화
            total = 0

            for idx2 in range(idx, idx+m):
                total += num_list[idx2]

            #  min_sum 초기값
            if idx == 0:
                min_sum = total

            # min_sum, max_sum 업데이트
            if total < min_sum:
                min_sum = total
            elif total > max_sum:
                max_sum = total

    result.append(max_sum-min_sum)

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))

