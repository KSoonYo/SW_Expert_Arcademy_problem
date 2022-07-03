import sys

sys.stdin = open('input.txt')

result = [0]
for _ in range(10):
    test_case = int(input())
    char_set = [list(input()) for _ in range(100)]
    longest_length = 1

    # 행과 열을 돌면서 현재 위치의 항목과 같은 부분을 찾음
    # 현재 위치의 항목과 같은 부분을 끝 지점으로 하여 회문 검사
    # 회문이 맞다면 해당 인덱스까지의 길이와 현재까지의 최대 길이를 비교하여 최대 길이 갱신
    for i in range(100):
        point = 0
        while point < 100:
            for j in range(point+1, 100):
                if char_set[i][point] == char_set[i][j]:
                    part_char_set = char_set[i][point:j+1]
                    if part_char_set[0:] == part_char_set[::-1] and len(part_char_set) > longest_length:
                        longest_length = len(part_char_set)
            point += 1

    # 전치
    char_set_T = [[''] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            char_set_T[i][j] = char_set[j][i]

    for i in range(100):
        point = 0
        while point < 100:
            for j in range(point+1, 100):
                if char_set_T[i][point] == char_set_T[i][j]:
                    part_char_set = char_set_T[i][point:j+1]
                    if part_char_set[0:] == part_char_set[::-1] and len(part_char_set) > longest_length:
                        longest_length = len(part_char_set)
            point += 1

    result.append(longest_length)

for print_case in range(1, 11):
    print('#{} {}'.format(print_case, result[print_case]))

"""
참고)

####

s1 = 'ABBC'  # = input()
# s1 = ['A', 'B', 'B', 'A'] # = list(input())

if s1 == s1[::-1]:
    print(1)
else:
    print(0)

M = len(s1)
ans = 1
for i in range(M//2): # 비교할 원소 중 왼쪽 인덱스
    # if s1[i] == s1[M-1-i]:
    if s1[i] != s1[M - 1 - i]:
        ans = 0 # 회문이 아닌 경우
        break # 비교대상이 다르면 회문이 아님
# 회문인 경우/아닌경우
print(ans)


####

s1 = 'XYABBAZ'  # = input()
N = len(s1)
M = 4 # 길이가 M인 회문이 존재하는가?

def palin(N, M, s1):
    for i in range(N-M+1): # 확인하려는 영역의 시작 인덱스
        flag = 1 # i에서 시작하는 영역이 회문이라 가정
        for j in range(M//2):
            if s1[i+j] !=  s1[i+M-1-j]: # 다르면 다음 영역으로...
                flag = 0
                break  # 회문이 아니면 다음 영역으로
        if flag: # 비교한 글자가 모두 같은경우
            return 1
    return 0 # 더이상 남은 영역이 없는 경우

print(palin(N, M, s1))


####

s1 = 'XYABCBAZ'  # = input()
N = len(s1)
#M = 4 # 길이가 M인 회문이 존재하는가?
# 가장 긴 회문? M = N, N-1, ...., 2
def palin(N, M, s1):
    for i in range(N-M+1): # 확인하려는 영역의 시작 인덱스
        flag = 1 # i에서 시작하는 영역이 회문이라 가정
        for j in range(M//2):
            if s1[i+j] !=  s1[i+M-1-j]: # 다르면 다음 영역으로...
                flag = 0
                break  # 회문이 아니면 다음 영역으로
        if flag: # 비교한 글자가 모두 같은경우
            return 1 # return i
    return 0 # 더이상 남은 영역이 없는 경우

for M in range(N, 1, -1):  # 가장 긴 회문부터 조사
    if palin(N, M, s1): # 회문이 존재하면
        print(M)
        break



####

def f(N, M, arr):
    for i in range(N): # i행에 회문이 있는 검사
        for j in range(N-M+1): # 확인할 영역의 시작 인덱스
            flag = 1 # 이번 영역이 회문이라 가정
            for k in range(M//2): # 비교할 왼쪽 원소의 인덱스
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = 0
                    break # 해당 영역 비교 중지
            if flag:
                #print(''.join(arr[i][j:j+M]))
                # for k in range(M):
                #     print(arr[i][j+k], end='')
                s = ''
                for k in range(M):
                    s += arr[i][j+k]
                return  s # 찾은 경우....
    for i in range(N): # i열에 회문이 있는 검사
        for j in range(N-M+1): # 확인할 영역의 시작 인덱스
            flag = 1 # 이번 영역이 회문이라 가정
            for k in range(M//2): # 비교할 왼쪽 원소의 인덱스
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    flag = 0
                    break # 해당 영역 비교 중지
            if flag:
                s = ''
                for k in range(M):
                    s += arr[j + k][i]
                return s  # 찾은 경우....

N, M = map(int, input().split()) # 문자열 길이, M 찾을 회문의 길이
arr = [list(input()) for _ in range(N)]
ans = f(N, M, arr)
print(ans)

"""
