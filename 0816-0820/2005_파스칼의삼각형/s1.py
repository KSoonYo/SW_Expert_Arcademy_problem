tests = int(input())

for tc in range(1, tests+1):
    N = int(input())

    triangle = [[1]]

    # 전략(아마도 dp..?)
    # 각 항목의 길이는 인덱스 + 1 만큼의 길이
    # 각 항목의 양쪽 끝 인덱스는 1
    # 각 항목의 내부는 현재 행의 열에서 -1 한 열과 이전 행의 동일한 열의 값을 합한 값으로 이루어짐

    for elem in range(1, N):
        add_elem = [0 for i in range(elem+1)]
        add_elem[0] = add_elem[-1] = 1
        for idx in range(1, len(add_elem)-1):
            left_elem = triangle[elem-1][idx-1]
            right_elem = triangle[elem-1][idx]
            add_elem[idx] = left_elem + right_elem
        triangle.append(add_elem)

    print('#{}'.format(tc))
    for outer_elem in triangle:
        print(*outer_elem)
    # 위 출력문은 아래 동작과 같음
    # for outer_elem in triangle:
    #     for inner_elem in outer_elem:
    #         print(inner_elem, end=' ')
    #     print('')

'''
메모이제이션 풀이

[재귀 형태]
pascals = [[] for _ in range(11)] # 메모이제이션
pascals[1].append([1])

def pascal(n): # 재귀를 통해 풀었다.
    if not pascals[n]: # 파스칼[n]이 비어있을 경우 다음과 같이 채운다.
        pascals[n] = pascal(n-1) # 일단 n이전 층을 불러온다.     [1,2,1]
        new_li = [0] * n # 이번에 새로 만들 층                   [1,3,3,1]
        last_li = pascals[n][-1] # n-1에서 만든 층
        for i in range(n-1): # n-1의 각 값을 같은 인덱스, 같은 인덱스+1에 더해준다.
            new_li[i] += last_li[i]
            new_li[i+1] += last_li[i]
        pascals[n].append(new_li) # 그렇게 만든 층을 쌓는다.

    return pascals[n]


'''




'''
보충 수업 solution)


# 이 문제는 n 개에서 r개를 고르는 조합을 구하는 문제 풀이 과정과 비슷하게 풀 수 있음 => n C r = n-1 C r-1 + n-1 C r
# n개 에서 r개를 뽑는 조합 수

# 2차원 배열로 풀이
# n x n 행렬
# i==0 or i==j 일때 p[i][j] = 1
# p[i][j] = p[i-1][j] + p[i-1][j-1] ( i > j and j != 0)
# i : 0 -> N-1, j: 0 -> i
# 문제에서 N의 최대값이 10으로 지정되어 있으므로 아예 10 x 10 파스칼의 삼각형을 하나 만들어 놓고 출력만 순차적으로 하는 방법
T = int(input())
p = [[0] * 10 for _ in range(10)] # 문제의 조건에서 최대 10줄
for i in range(10):
    for j in range(i+1): 
        if j == 0 or i == j: # 각 행의 0번째, p 리스트에서 (0,0) 부터 대각선 방향에 있는 인덱스는 모두 1
            p[i][j] = 1
        else:
            p[i][j] = p[i-1][j-1] + p[i-1][j]


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(p[i][j], end = ' ')
        print()
'''






