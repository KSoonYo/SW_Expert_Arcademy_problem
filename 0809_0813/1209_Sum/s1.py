import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    # 입력
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합의 최댓값
    # s = 0
    # # 대각선 원소의 합
    # for i in range(100):
    #     s += arr[i][i] # 우하향 대각선 원소 접근
    # maxV = s
    #
    # s = 0 # 왼쪽 아래 대각선의 합
    # for i in range(100):
    #     s += arr[i][99-i]
    # if maxV < s:
    #     maxV = s

    # 위 두 과정을 결합
    s1 = 0
    s2 = 0
    for i in range(100):
        s1 += arr[i][i]
        s2 += arr[i][99-i]

    maxV = s1
    if maxV < s2:
        maxV = s2
    # 양 대각선의 합은 각각 하나씩만 있음!

    # # 행의 합
    # for i in range(100):
    #     s = 0
    #     for j in range(100):
    #         s += arr[i][j] # i행의 합
    #
    #     if maxV < s:
    #         maxV = s
    #
    # # 열의 합
    # for j in range(100):
    #     s = 0
    #     for i in range(100):
    #         s += arr[i][j]
    #     if maxV < s:
    #         maxV = s

    # 행의 합과 열의 합
    for i in range(100):
        s1 = 0
        s2 = 0
        for j in range(100):
            s1 += arr[i][j] # 행의 합
            s2 += arr[j][i] # 열의 합
        if maxV < s1:
            maxV = s1
        if maxV < s2:
            maxV = s2

    print('#{} {}'.format(tc, maxV))
