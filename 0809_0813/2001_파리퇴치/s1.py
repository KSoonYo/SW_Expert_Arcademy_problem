# import sys

# sys.stdin = open('input.txt')

TEST = int(input())
result = []


for test_case in range(1, TEST+1):
    N, M = map(int, input().split())

    # N x N 행렬 
    area = [[0 for _ in range(N)] for _ in range(N)]

    # 행렬 내 요소 값 입력
    # [[0,0,0], [0,0,0], [0,0,0]] => 3x3 행렬
    for row in range(len(area)):
        area[row] = list(map(int, input().split()))



    top_value = area[0][0]

    # 지도 순회
    for row in range(N-M+1):
        for column in range(N-M+1):
            total_sum = 0
    
            # 파리채 크기 M x M
            # 파리채 가장 왼쪽 상단을 시작점으로 하여 파리채 크기만큼 내부의 값들을 모두 더함
            # [row][column] [row][colum++] [row++][column] [row++][column++] 순으로 더함
            for r in range(row, row + M):
                for c in range(column, column + M):
                    total_sum += area[r][c]
            
            if total_sum > top_value:
                top_value = total_sum
    
    result.append(top_value)

for idx, value in enumerate(result):
    print(f'#{idx+1} {value}')