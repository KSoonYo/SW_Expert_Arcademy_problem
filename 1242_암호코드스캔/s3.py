import sys
sys.stdin = open('sample_input.txt')

"""
나의 실수
1. 16진수의 rstrip은 의미가 없음
2. 2진법 변환 과정에서 0을 '0'으로 추가하는 대신 '0000'으로 넣어줘야 함
3. visited 변수를 만들어 주어 검증된 암호가 2번 더해질 일을 없게 만들어야 함
4. 109번 line의 조건문을 나누어서 변수 초기화를 적절히 해줘야 함
"""

T = int(input())

# 0과 1의 비율이 key
# decoding_table
decoding_table = {
    '211': 0, '221': 1, '122': 2,
    '411': 3, '132': 4, '231': 5,
    '114': 6, '312': 7, '213': 8,
    '112': 9
}

htob = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

def is_checked(decoded_list):
    check_list = [0] + decoded_list
    odd_num = []
    even_num = []
    for i in range(1, len(check_list) - 1):
        if (i & 1):  # i가 홀수
            odd_num.append(check_list[i])
        else:  # i가 짝수
            even_num.append(check_list[i])

    # 검증식
    to_check = (sum(odd_num) * 3) + sum(even_num) + check_list[-1]

    if to_check % 10:
        return False
    return True

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = []

    # 배열 입력
    original_code = [input().strip() for _ in range(N)]

    # 중복 제거
    original_code = set(original_code)
    final_result = 0

    while original_code:
        result = []  # 각 줄의 암호코드를 담을 리스트

        each_row = original_code.pop()
        if each_row == '':
            continue
        # 16진수 -> 2진수
        binary_code = ''
        for idx in range(len(each_row)):
            hex_num = each_row[idx]
            binary_code += htob[hex_num]

        # 오른쪽 0 제거
        binary_code = binary_code.rstrip('0')

        # 뒤에서부터 1과 0을 센다.
        # 1 -> 0, 0 -> 1 지점 주의
        # 1 다음에는 반드시 0, 0 다음은 반드시 1, 1 다음은 또 0
        # 1 -> 0 -> 1 -> 코드 숫자 한 개 시작점 (전환이 총 3번 이루어짐)
        code_length = 0  # 코드 하나의 이진코드 길이(최소 길이 7)
        code_length_n = 0  # 배수

        idx = len(binary_code) - 1
        temp = []
        decoded_list = []
        n1 = n2 = n3 = 0
        while idx > -1:
            if n2 == 0 and n3 == 0 and binary_code[idx] == '1':  # 뒤에서 보는 첫 1
                n1 += 1
            elif n1 and n3 == 0 and binary_code[idx] == '0':  # 뒤에서 두번째 0
                n2 += 1
            elif n1 and n2 and binary_code[idx] == '1':  # 뒤에서 세번째 1
                n3 += 1

            # 최소 길이 7 => 56
            ###   0001   0000000b0000
            # decodieng
            if n1 and n2 and n3 and binary_code[idx] == '0':
                temp = [n3] + [n2] + [n1] + temp

                # 코드 숫자 하나의 이진코드 길이, 배수 구하기
                code_length_n = min(temp)

                key = str(temp[0] // code_length_n) + str(temp[1] // code_length_n) + str(temp[2] // code_length_n)
                decoded_value = decoding_table.get(key)
                if decoded_value is None:
                    temp = []
                    n1 = n2 = n3 = 0
                    continue
                decoded_list = [decoded_value] + decoded_list
                temp = []
                n1 = n2 = n3 = 0
            temp_s = ''.join(map(str, decoded_list))
            # 검증
            if len(decoded_list) == 8:
                if is_checked(decoded_list) and temp_s not in visited:
                    final_result += sum(decoded_list)
                visited.append(temp_s)
                temp_s = ''
                decoded_list = []
            idx -= 1
    print('#{} {}'.format(tc, final_result))

