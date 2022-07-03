import sys
sys.stdin = open('input.txt')
tests = int(input())
# 재귀로 시행될 때마다 L과 R을 입력받는다.
# change_box의 인자 중 i는 (1<= i <= Q)
def change_box(Q, i, prior_list):
    if i > Q:
        return prior_list

    L, R = map(int, input().split())
    # 주의: L과 R을 각각 하나씩 빼야 리스트 내 박스 위치를 정확하게 가리킬 수 있다.
    # 리스트는 0번째부터 위치가 시작되기 때문

    # change 작업
    # L은 항상 1보다 크거나 같기 때문에 for문의 첫 시작이 -1이 될 걱정은 없다.
    # R 역시 N보다 항상 작거나 같으므로 인덱스 범위를 벗어날 일이 없다!
    for idx in range(L-1, R):
        prior_list[idx] = i
    i += 1
    return change_box(Q, i, prior_list)

result = [0]
for _ in range(tests):
    N, Q = map(int, input().split())
    original_list = [0] * N
    int_result_list = change_box(Q, 1, original_list)

    # 정수형 요소를 string으로 변환해주는 작업
    str_result_list = list(map(str, int_result_list))
    result.append(str_result_list)

# unpack 연산자 * 활용 가능 => *result, 단 format이 안되기 때문에 print('#{} {}'.format, *result)로 구분해서 사용해야!
# list의 각 요소를 사이에 공백을 두면서 unpack이 된다.(type에 상관없이!) => .join만큼 유용

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, ' '.join(result[print_case])))