import sys

sys.stdin = open('input.txt')


# 열이 절대 겹치면 안된다!
def get_cost(row, cost, min_cost, factory):
    
    now_cost = cost
    if now_cost > min_cost:
        return min_cost

    if row > N:
        return min(now_cost, min_cost)
    
    
    for idx in range(1, N+1):
        if idx in factory:
            continue
        next_cost = now_cost + V[row][idx]
        factory.append(idx)
        min_cost = get_cost(row+1, next_cost, min_cost, factory)
        factory.pop()

    return min_cost


for tc in range(1, int(input())+1):

    N = int(input())
    
    # 편하게 인덱스 1 부터 값이 시작된다.
    V = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    # 최소비용 찾기
    min_cost = 99 ** 2 # 최소비용 초기화
    factory = []
    result = get_cost(1, 0, min_cost, factory)
    print('#{} {}'.format(tc, result))
