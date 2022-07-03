
for tc in range(1, int(input())+1):
    N = float(input())
    result = ''

    # 10 진수 N의 소수 부분이 모두 0될 때까지 N의 소수부분에 2를 계속 곱해준다.
    # 위에서부터 차례대로 정수부분을 읽으면 2진수 완성
    binary_result = ''
    to_float = 1
    while True:
        under_dot = N - int(N)
        if len(binary_result) > 12: # 최대 이진수 소수점 자리는 12자리
            break
        if under_dot == 0:
            break
        N = under_dot * 2
        binary_result += str(int(N))
        to_float += 1

    # print('to_float: ', to_float)
    # print('binary length: ', len(binary_result))

    if len(binary_result) > 12:
        result = 'overflow'
    else:
        result = binary_result
    print('#{} {}'.format(tc, result))
