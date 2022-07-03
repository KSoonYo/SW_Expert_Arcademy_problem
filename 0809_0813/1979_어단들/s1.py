import sys

sys.stdin = open('input.txt')




def blank_finding(cnt, N, K, square):
    here_cnt = cnt
    row = 0
    while row < N:
        row_square = square[row]
       
        # idx가 0이라면 범위 오른쪽에 0이 있는지 확인 
        # idx가 N-K라면, 범위 왼쪽에 0이 있는지 확인
        # idx가 0 < idx < N-K 라면, 범위 양쪽에 0이 있는지 확인 
        # 모래 주머니 풀자...
        for idx in range(N-K+1):
            temp_list = row_square[idx:idx+K]
            blank = 0
            for elem in temp_list:
                if elem:
                    blank += 1

             # idx가 0이라면 범위 오른쪽에 0이 있는지 확인 
            if blank == K and idx == 0:
                if not row_square[idx+K]:
                    here_cnt += 1

            # idx가 N-K라면, 범위 왼쪽에 0이 있는지 확인
            elif blank == K and idx == N-K:
                if not row_square[idx-1]:
                    here_cnt += 1
            
            # idx가 0 < idx < N-K 라면, 범위 양쪽에 0이 있는지 확인 
            else:
                if blank == K and (not row_square[idx-1]) and (not row_square[idx+K]):
                    here_cnt += 1
        row += 1

    return here_cnt
    

tests = int(input())


result = [0]
for _ in range(tests):
    N, K = map(int, input().split())
    # N x N 정사각형

    square = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        square[i] = list(map(int, input().split()))
    

    cnt = 0
    cnt = blank_finding(cnt, N, K, square)

    # 전치
        
    for i in range(N):
        for j in range(N):
            if i < j:
                square[i][j], square[j][i] = square[j][i], square[i][j]
            
    cnt = blank_finding(cnt, N, K, square)
  
    result.append(cnt)

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))


'''
효율적인 해결방법)

import sys
sys.stdin = open('input.txt')

T = int(input())
"""
전략: 행과 열을 0을 기준으로 스플릿한다. 리스트를 순회하며 길이가 K 인 것을 찾으면 끝~~ 
"""
for test_case in range(1, T+1):

    N, K = map(int, input().split())

    #문자열을 그대로 받음

    #행 모음 (중간 공백 삭제)
    rows = [input().replace(' ','') for _ in range(N)]

    #열 모음 (zip을 통해 행을 열로 변환)
    cols = [''.join(num) for num in zip(*rows)]

    #들어갈 수 있는 단어 세기 초기화
    cnt = 0

    #행을 불러옴
    for row in rows:
        row = row.split('0') #0을 기준으로 쪼개서 리스트를 생성
        for sells in row : #쪼갠 리스트를 탐색
            if len(sells) == K: #셀들의 길이가 K면 카운트 + 1
                cnt += 1

    #열을 불러움
    for col in cols:
        col = col.split('0') #0을 기준으로 쪼개서 리스트를 생성
        for sells in col: #쪼갠 리스트 탐색
            if len(sells) == K : #셀들의 길이가 K면 카운트 + 1
                cnt += 1

    print('#{} {}'.format(test_case, cnt))

    by 두회님 풀이

'''

                    