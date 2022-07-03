
    # 16진수가 있는 배열 한 줄에 암호코드가 1개 이상 있음
    # 전체 암호코드의 최소 가로 길이는 56
    # 암호코드의 각 숫자의 최소 칸 수는 7칸

    # 암호코드의 가로 길이가 56 * n 인 경우, 암호코드의 각 숫자의 최소 칸 수도 7 * n
    # 배열은 모두 16진수로 이루어져 있음
    # 세부 배열 하나에 암호코드 1개 이상 있을 수 있다.(암호 코드 사이에는 0으로 빈공간이 있음)


import sys

sys.stdin = open('sample_input.txt')


# 0과 1의 비율이 key    
# decoding_table
decoding_table = {
        '211':0, '221':1, '122':2,
        '411':3, '132':4, '231':5,
        '114':6, '312':7, '213':8,
        '112':9
    }

def decoder(binary_code):
    '''
    암호를 해석하는 함수
    '''
    # print('binary_code', binary_code)
    code_length = 0 # 암호 코드 숫자 하나의 길이
    code_length_n =  0 # 코드 길이 배수

    # 뒤에서부터 요소의 개수를 count
    temp = []
    idx = -1
    target_binary_code = binary_code
    value_cnt = 0
    next_start = True
    decoded_values = []
    while abs(idx) <= len(binary_code) :      
        if target_binary_code[idx] == '1':
            next_start = True

        if not next_start:
            idx -= 1
            continue

        current_value = target_binary_code[idx]
        pre_value = '1'
        
        if idx < -1:
            pre_value = target_binary_code[idx+1]

        if pre_value != current_value:
            # 1 -> 0 혹은 0 -> 1 전환지점이 나오면
            # temp에 누적
            temp = [value_cnt] + temp
            value_cnt = 1
        else:
            value_cnt += 1

        if len(temp) == 3:
            if not code_length_n:
                code_length_n = min(temp) 
                code_length = 7 * code_length_n # 암호코드 한 개의 최소 길이가 7이므로
                if tc == 7:
                    print('code length_n', code_length_n)
                    print('code_length', code_length)
            if tc == 7:
                print('temp:', temp)
            key = str(temp[0] // code_length_n) + str(temp[1] // code_length_n) + str(temp[2] // code_length_n)
            # print('idx', idx, 'key', key)
            if decoding_table.get(key) is None: # (주의)is None으로 안하고 not으로 하면 value가 0일 때 이 조건문이 실행된다.
                if tc == 7:
                    print('not found key value')
                    print('key: ', key)
                return None, idx # 비정상 암호 코드
            decoded_values = [decoding_table.get(key)] + decoded_values
            temp = []
            next_start = False
        
        if len(decoded_values) == 8 and is_checked(decoded_values):
            return decoded_values, idx

        elif len(decoded_values) == 8 and (not is_checked(decoded_values)):
            return None, idx

        idx -= 1
  



def is_checked(decoded_list):
    check_list = [0] + decoded_list
    odd_num = []
    even_num = []
    for i in range(1, len(check_list)-1):
        if (i & 1): # i가 홀수
            odd_num.append(check_list[i])
        else: # i가 짝수
            even_num.append(check_list[i])

    # 검증식
    to_check = (sum(odd_num) * 3 ) + sum(even_num) + check_list[-1]
    
    if to_check % 10:
        return False
    return True




for tc in range(1, int(input())+1):
    # if tc == 7:
    #     sys.stdout = open('7th_input.txt', 'w')

    ##### 전략 ######
    
    #### 2진수 변환 + 암호 해독

    # 1. 가장 끝 0들을 모두 rstrip으로 지워준다. 
    # 2. 0이 아닌 숫자들을 pop() 으로 모두 가져온다.(끝에서부터 가져오기.)
    # 3. 16 진수를 모두 2진수로 바꾼다. 
    # 4. 마지막 0들을 모두 쳐낸다.
    # 5. 길이가 56으로 나누어 떨어지지 않는다면 나누어 떨어질 때까지 이전 배열에서 pop()을 한다. 
    # 6. 길이가 56으로 나누어 떨어진다면 코드 decoding 과정으로 넘어간다.     
    # 7. decoding 된 코드가 유효하다면 리스트에 저장해놓고 다른 암호를 찾음
    # 8. 이전 배열에서 rstrip으로 오른쪽 0을 모두 날려준다.
    # 9. 남은 배열에서 숫자가 남아있다면 2번 과정으로 넘어간다.(남은 숫자가 더 없으면 다음 줄로)
    # 10. 최소 길이가 안되는데 pop()할 것이 없다면 유효하지 않은 코드이므로 다음 줄로 넘어간다. 

    
    ######

    # N : 세로 길이 / M : 가로 길이
    N, M = map(int, input().split())
   
    # 배열 입력받기
    original_code = [input().rstrip('0') for _ in range(N)]
    if tc == 7:
        print('original_code')
        print(original_code)

    # 테스트케이스 1개 암호코드 결과 set
    result = []

    # 출력 결과
    final_result = 0

    # 한 줄씩 순회
    for each_row in original_code:
        # 0 모두 제거
        if each_row == '':  # 남는 게 없다면 다음 줄로
            continue

        if tc == 7:
            print('7th each row', each_row)
        each_list = list(each_row) # each_row 문자열들을 요소 별로 분화해서 list 형변환
        target_list = list(each_row)

        # 16진수 -> 2진수
        for idx in range(len(each_list)):
            if each_list[idx] == '0':
                continue
            hex_n = each_list[idx]
            target_list[idx] = format(int('0x'+hex_n, 16), 'b').zfill(4)
  
        binary_code = ''.join(target_list).rstrip('0')
        if tc == 7:
            print('7th binary_code', binary_code)

        while binary_code:
            decoded_result = decoder(binary_code)
            if not decoded_result:
                break

            if decoded_result[0] and (decoded_result[0] not in result): # 해석값이 있고 중복되지 않는다면
                if tc == 7:
                    print('add result list')
                result.append(decoded_result[0])
            binary_code = binary_code[decoded_result[1]::-1]
            binary_code = binary_code[::-1]
            binary_code = binary_code.rstrip('0')
            if tc == 7:
                print('next binary code', binary_code)

        if tc == 7:
            print('7th result list', result)
        
    for result_code in result:
        final_result += sum(result_code)
    
    if tc != 7:
        continue
    print('#{} {}'.format(tc, final_result))
    

           
                
    
