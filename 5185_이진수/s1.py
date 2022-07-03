

for tc in range(1, int(input())+1):
    N, hex_num = input().split()
    
    binary_result = ''

    # 2진수 변환
    for idx in range(int(N)):
        # 한 자리씩 끊기
        if hex_num[idx] in list(map(str, range(0, 10))):
            # 1 ~ 9
            temp = int(hex_num[idx])
        else:
            # 'A'~ 'F'
            temp = ord(hex_num[idx]) - 65 + 10
        
        # print('temp: ', temp)

        # 16진수 자리 하나는 2진수 4자리 => 4개의 비트로 표현
        # >> 연산자와 & 연산으로 맨앞 비트부터 차례로 binary_result에 결합
        
        # for i in range(3,-1, -1):
        #     # print('현재 temp의 2진수: ', str(((temp >> i) & 1)))
        #     binary_result += str(((temp >> i) & 1))
        #     # print('binary_result: ', binary_result)

        # 한번에 통으로 결합하기
        binary_result += str(temp >> 3 & 1) + str(temp >> 2 & 1) + str(temp >> 1 & 1) + str(temp & 1)
      
    print('#{} {}'.format(tc, binary_result))