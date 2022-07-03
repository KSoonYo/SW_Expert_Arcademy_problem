import sys

sys.stdin = open('input.txt')


code_patterns = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}



def to_code(pre_code):
    '''
    입력 코드에서 7자리씩 코드를 끊어서 가져오는 함수
    '''
    result_code = []
    
    # 끝자리부터 검사하여 1이 나올 때까지 idx -= 1 (암호코드의 맨 마지막 숫자가 반드시 1 이므로)
    start_idx = len(pre_code) - 1
    end = -1
    idx = start_idx
    while idx > end:
        if pre_code[idx] == '1':
            break
        idx -= 1

    # 가장 끝자리부터 7자리씩 끊어서 저장 후 result_code에 저장
    temp = ''
    for code_idx in range(idx, -1, -1):
        if len(result_code) == 8: # 결과 코드가 8자리가 되었다면
            break
        
        temp += pre_code[code_idx]

        if len(temp) == 7: # 코드 7자리가 다 모였다면
            result_code.append(temp[::-1]) # 끝자리부터 합쳤으므로 합친 문자열을 뒤집어서 리스트에 추가
            temp = ''

    # print('result_code: ', result_code)
    if len(result_code) < 8: # 결과 코드가 8개 이내라면 
        return 0 # 비정상적 암호
    
    return list(reversed(result_code)) # 마찬가지로 끝 7자리부터 append하였으므로 뒤집어서 반환


def decoder(check_list):
    # print('check_list: ', check_list)
    checked_list = []
    for checked_code in check_list:
        if code_patterns.get(checked_code) is None:
            # print('checked_code', checked_code)
            return None
        checked_list.append(code_patterns.get(checked_code))
    
    return checked_list

def is_check(final_result):
    '''
    코드가 암호코드인지 검증하는 함수
    암호 코드의 각 코드 자리 검증 ( 7 자리와 1 자리 검증코드)
    검증식:  “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수
    10의 배수이면 정상적인 암호코드, 아니면 비정상적인 암호코드
    '''
    final_result = [0] + final_result # 0번째 인덱스는 무의미한 값
    odd_num = []
    even_num = []
    for i in range(1, len(final_result)-1): # 마지막 자리의 코드는 검증 코드
        # i가 짝수라면 0, i가 홀수라면 1
        if (i & 1): # i가 홀수라면
            odd_num.append(final_result[i])
        else: # i가 0 혹은 짝수라면
            even_num.append(final_result[i])
        # print('i: ', i, final_result[i])
    # print('odd_num: ', odd_num)
    # print('even_num: ', even_num)

    # 검증식
    to_check = (sum(odd_num) * 3 ) + sum(even_num) + final_result[-1]
    
    if to_check % 10: # 검증식 결과가 10으로 나누어 떨어지지 않으면
        return False # 비정상
    return True # 10으로 나누어 떨어지면 정상

for tc in range(1, int(input())+1):
    result = 0
    # N : 배열의 세로크기 | M : 배열의 가로크기
    N, M = map(int, input().split())
    
    # 배열 입력 받기
    input_codes = [input() for _ in range(N)]
    
    # 배열 순회
    for code in input_codes:
        if code.count('1') <= 3: # code에 1이 3개 이하라면
            continue
        
        # 입력 코드 배열을 7자리씩 끊어서 다듬기
        necessary_check = to_code(code)
        # print('necessary_check: ', necessary_check)
        if not necessary_check: # 비정상적 코드라면
            continue

        # 얻어낸 코드를 숫자로 decoding
        decoded_code = decoder(necessary_check)
        # print(decoded_code)
        if not decoded_code: # 비정상 코드라면 
            continue

        # 다듬은 코드를 검증하기
        if is_check(decoded_code): # 정상적인 암호 코드라면
            result = sum(decoded_code)
            break
    
    print('#{} {}'.format(tc, result))

