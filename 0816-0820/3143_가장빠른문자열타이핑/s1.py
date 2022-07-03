import sys

sys.stdin = open('sample_input.txt')

tests = int(input())

result = [0]
for _ in range(tests):
    A, B = input().split()
    typed_char = ''

    # A문자열 내에 B의 개수
    count_b = A.count(B)

    # A 전체 문자 개수
    count_A = len(A)

    # B 전체 문자 개수
    count_B = len(B)

    # B 없이 치는 A 타이핑 수에 (B전체 문자 개수를 빼주고 + 1) * count_b 만큼
    typed_count = count_A - (count_B - 1) * count_b
    result.append(typed_count)

    # typed_char 가 A와 동일할 때까지
    # A 문자열을 돌면서 B의 각 문자들과 동일한지 check(고지식한 알고리즘 활용)
    # 동일한 것이 없다면 해당 문자를 type 하고 횟수 +1
    # 동일한 것이 있다면 B를 type 하고 횟수 +1
    # i = 0
    # j = 0
    # while typed_char != A or i < len(A):
    #     if A[i] != B[j]:
    #         i -= j
    #         j = -1
    #         typed_char += A[i]
    #         count += 1
    #     i += 1
    #     j += 1
    #
    #     if j == len(B):
    #         count += 1
    #         typed_char += B
    #         j = 0

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))




