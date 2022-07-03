
tests = int(input())

result = [0]
for _ in range(tests):
    N = int(input())

    # dp 문제
    # 시뮬레이션을 통해 N에 따라 변화하는 규칙을 찾고 점화식을 세움
    # N = 10 => 1 / N = 20 => 3 / N = 30 => 5 / N = 40 => 11 ...
    # f(N) = f(N-1) + f(N-2) * 2
    '''
    추가 설명)

    20 x 10 상자 a와 20 x 20 상자 b가 기본으로 있음
    
    ###
    N이 20이면

    20 x 10 상자 a를 쓰는 경우의 수 2 + 20 x 20 상자 b를 스는 경우의 수 1 = 3
    
    ###
    N이 30이면

    N이 20인 경우에서 오른쪽으로 20 x 10 상자를 하나씩 더 붙인 경우의 수 : 3 
    +
    N이 10인 경우에서 오른쪽으로 20 x 20 상자를 붙이는 경우의 수
     # 왼쪽으로 붙이면 앞서 오른쪽으로 붙였을 때와 중복되는 경우 발생
    (상자 a를 가로로 눕혀서 붙이는 경우, 20x20 상자 b 하나를 쓰는 경우)
    : 2
    = 5
    
    ###
    N이 40이면

    N이 30인 경우에서 오른쪽으로 20 x 10 상자를 하나씩 더 붙인 경우의 수 : 5
    +
    N이 20인 경우에서 오른쪽으로 20 x 20 상자를 붙이는 경우의 수 
    (상자 a를 가로로 눕혀서 붙이는 경우, 20x20 상자 b를 쓰는 경우) : 3 x 2 = 6
    = 11


    '''


    # N에 따른 결과값을 저장할 리스트
    # # N의 인덱스 화
    N = N // 10
    square = [0 for _ in range(N+1)]
    square[1] = 1
    square[2] = 3
    # 점화식을 바탕으로 sqaure 값을 채워넣음
    for idx in range(3, N+1):
        square[idx] = square[idx-1] + square[idx-2] * 2

    result.append(square[N])

for tc in range(1, tests+1):
    print('#{} {}'.format(tc, result[tc]))

