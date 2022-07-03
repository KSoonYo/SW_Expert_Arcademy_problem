import sys

sys.stdin = open('input.txt')

def get_prim_number(num):
    count_list = [0] * 5
    div_numbers = [2, 3, 5, 7, 11]

    # div_numbers의 소수들로 나누기
    # 나눈 몫이 1이 될 때까지 반복

    # div_number의 인덱스를 가리킬 변수 idx
    idx = 0
    while num > 1:
        # div_numbers의 현재 위치 수에서 나눠지면(나머지가 0이 되면) idx는 그 자리에서 머무르고
        # 나머지가 0이 되지 않으면 다음 idx 요소로 넘어간다.
        # div_numbers의 전부를 돌아도 num이 1이 되지 않으면 break
        if idx == len(div_numbers):
            break

        if num % div_numbers[idx] == 0:
            # 각 위치에서 나눠질 때마다 count_list의 인덱스에서 +1
            num //= div_numbers[idx]
            count_list[idx] += 1
        else:
            idx += 1
    return count_list


tests = int(input())

result = [0]
for _ in range(tests):
    num = int(input())
    int_result_elem = get_prim_number(num)
    # 요소 문자열 변환 작업
    str_result_elem = list(map(str, int_result_elem))
    result.append(str_result_elem)

for print_case in range(1, tests + 1):
    print('#{} {}'.format(print_case, ' '.join(result[print_case])))