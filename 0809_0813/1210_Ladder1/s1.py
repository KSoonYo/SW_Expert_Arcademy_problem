from abc import abstractproperty
import sys

sys.stdin = open('input.txt')




result = [0]
for _ in range(10):
    # 위 오 아래 왼 (순서대로 시계방향)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    # 사다리 그림판
    paper = [[0 for _ in range(100)] for _ in range(100)]

    test_cases = int(input())

    # 차례대로 줄을 입력받고, 해당 줄의 1을 그림판에 그림
    for i in range(100):
        paper[i] = list(map(int, input().split()))

    # => paper을 한 열째로 입력을 받아서 한번에 리스트를 입력받는 방법
    """
    
    paper = [list(map(int, input().split())) for _ in range(100)]

    """

    
    # 전략
    # 첫 행의 줄이 1인 곳에서만 시작.
    # 진행 방향이 아래일 때는 현재 위치의 좌우를 탐색하고 좌 우 중에 1이 있으면 그곳으로 방향 전환
    # 좌 우 방향일 때 갈 수 없는 곳에 직면하면 아래로 방향 전환
    # 2를 만나면 만났을 때의 출발지점 x를 출력
     
    start_j = 0 # 시작 열
    while start_j < 100:
        dir = 2 # 아래 방향
        i = 0 # 첫 줄
        flag = False # 깃발
        if paper[i][start_j]:

            # 아래로 갈 수 있는 가장 마지막 칸은 99. 시작: 0, 끝: 99
            # 단, 좌 우로 방향 전환 할 때에는 아래로 가는 횟수가 늘어나지 않음.
            r = 0
            j = start_j
            while r < 99:
                nr, nj = r + di[dir], j + dj[dir] # 칸 이동, nr, nj는 이동할 칸 지정
                if dir == 2:
                    left, right = nj + dj[dir+1], nj + dj[dir-1]

                # 이동할 칸이 100x100 영역 안에 있고, 해당 칸의 값이 0이 아닌 경우
                if 0 <= nr < 100 and 0 <= nj < 100 and paper[nr][nj]:
                        
                    # 좌우 탐색
                    # 아래 방향 중에 왼쪽에 1이 있으면
                    if dir == 2 and 0 <= left < 100 and paper[nr][left]:
                        # 왼쪽으로 방향 전환
                        dir = (dir + 1) % 4

                    # 아래 방향 중에 오른쪽에 1이 있으면
                    elif dir == 2 and 0 <= right < 100 and paper[nr][right]:
                        # 오른쪽으로 방향 전환
                        dir = (dir - 1) % 4
                    
                    # 방향 유지
                    r, j = nr, nj

                    # 2를 만날 경우(종점)
                    if paper[nr][nj] == 2:
                        flag = True

                # 이동한 칸이 영역 안에 없다면
                else:
                    # 좌 우로만 움직이므로 현재의 방향은 좌 우뿐
                    # 따라서 방향을 아래로 전환시켜준다.
                    dir = 2
               
        if flag:
            result.append(start_j)
            break 

        start_j += 1

for print_case in range(1, 11):
    print('#{} {}'.format(print_case, result[print_case]))