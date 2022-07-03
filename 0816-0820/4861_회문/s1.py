import sys

sys.stdin = open('sample_input.txt')

tests = int(input())

result = [0]
for _ in range(tests):
    # N x N 행렬
    N, M = map(int, input().split())

    # 문자 입력
    char_list = [['' for _ in range(N)] for _ in range(N)]
    for row in range(N):
        char_set = input()
        for col in range(N):
            char_list[row][col] = char_set[col]

    # 행과 열을 M 길이에 맞춰서 문자열 비교 검사
    # 한 행의 문자열 길이 : N
    # 비교 문자열의 길이 : M
    flag = False
    checked = []
    for row_check in range(N):
        idx = 0
        while (idx+M)-1 < N:
            check_list = char_list[row_check][idx:(idx+M)]
            if check_list[0:] == check_list[::-1]:
                flag = True
                checked.append(''.join(check_list))
                break
            idx += 1
        if flag:
            result.append(checked[0])
            break

# 코드 개선점: for - else 구문을 사용하면 if not 조건문을 굳이 쓰지 않아도 괜찮다.(break를 만나지 않으면 else 구문 실행)

    if not flag:
        # 전치 후 동일 작업 시행
        # 개선점: zip() 활용한 전치
        # char_list = list(zip(*char_list))
        # 단 zip을 쓰려면 각 열의 내부 원소들의 갯수가 모든 행에서 동일해야 한다.
        for i in range(N):
            for j in range(N):
                if i < j:
                    char_list[i][j], char_list[j][i] = char_list[j][i], char_list[i][j]

        for row_check in range(N):
            idx = 0
            while (idx+M)-1 < N:
                check_list = char_list[row_check][idx:(idx+M)]
                if check_list[0:] == check_list[::-1]:
                    flag = True
                    checked.append(''.join(check_list))
                    break
                idx += 1
            if flag:
                result.append(checked[0])
                break

"""
슬라이싱을 사용하지 않은 문제 풀이법

sol1)

# 입력값 받아오기 및 변수 초기화
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''

    # N * N 문자열 반복
    # 한쪽 방향은 찾을 문자열 길이만큼 빼주고 반복
    for i in range(N):
        for j in range(N - M + 1):

            # 가로방향에서 회문이 있는지 탐색
            # 문자열의 양끝을 비교하여 다를 경우 반복문을 빠져나가게 만듬
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    break

            # 반복문이 break 를 만나지 않았다면 회문이므로 result 에 저장
            else:
                for k in range(M):
                    result += arr[i][j + k]

            # 세로방향에서 회문이 있는지 탐색
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    break
            else:
                for k in range(M):
                    result += arr[j + k][i]
    print('#{} {}'.format(test_case, result))

####

so2)

# 회문인지 확인하는 함수
def is_aba(st):
    for i in range(len(st) // 2):
        if st[i] != st[- i - 1]:
            return False
    return True

def abcdcba(n, m):
    li = [input() for _ in range(n)]
    for i in range(n): # 검사할 행,열의 인덱스
        for j in range(n - m + 1): # 회문의 시작 단어 위치
            st_r = '' # 가로로 찾을 string
            st_c = '' # 세로로 찾을 string
            for k in range(m): # m의 길이만큼 str을 쌓는다.
                st_r += li[i][j+k]
                st_c += li[j+k][i]
            # 찾은 글자가 회문이면 return
            if is_aba(st_r):
                return st_r
            elif is_aba(st_c):
                return st_c


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, abcdcba(N, M)))


"""



for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))
"""

    # 행과 열을 M 길이에 맞춰서 문자열 비교 검사
    # 한 행의 문자열 길이 : N
    # 비교 문자열의 길이 : M
    flag = False
    checked = ''
    for row_check in range(N):
        idx = 0
        while (idx+M)-1 < N:
            check_list = char_list[row_check][idx:(idx+M)]
            if check_list[0:] == check_list[::-1]:
                flag = True
                checked += check_list
                break
            idx += 1
        if flag:
            result.append(checked)
            break
    if not flag:
        # 열 체크
        for col in range(N):
            row = 0
            while (row + M) - 1 < N:
                up = ''
                down = ''
                if M % 2:
                    for up_row_check in range(row, (row+M)//2+1):
                        up += char_list[up_row_check][col]
                    for down_row_check in range((row+M)-1, (row+M)//2-1, -1):
                        down += char_list[down_row_check][col]
                else:
                    for up_row_check in range(row, (row+M)//2):
                        up += char_list[up_row_check][col]
                    for down_row_check in range((row+M)-1,(row+M)//2-1, -1):
                        down += char_list[down_row_check][col]
                if up == down:
                    down = down[::-1]
                    up_down = up + down
                    result.append(up_down)
                    flag = True
                    break
                row += 1
            if flag:
                break

for print_case in range(1, tests):
    print('#{} {}'.format(print_case, result[print_case]))

# 런타임 에러
"""





