import sys

sys.stdin = open('sample_input.txt')

# 순열 구하는 tip)
# from itertools import permutations 라이브러리로 쉽게 순열을 구할 수 있다.

def route_search(level, start, temp):
    
    # 경로 누적
    temp += [start]
 
    if level == (N-1):
        route.append(temp+[1])
        return

    # 방문 처리
    nodes[start] = 1

    # 후보군 색출
    candidates = []
    for target in range(2, N+1):
        if not nodes[target]:
            candidates.append(target)
    for candidate in candidates:
        route_search(level+1, candidate, temp)
        temp.pop()

    nodes[start] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    
    # 베터리 리스트
    battery = [[0] * (N+1)]  + [[0] + list(map(int, input().split())) for _ in range(N)]

    # 노드 리스트
    nodes = [0] * (N+1)

    # 경로 리스트
    route = []
    route_search(0, 1, temp=[])

    min_v = 100 ** 2
    for one_route in route:
        node_start = 0
        node_end = 1
        temp = 0
        for _ in range(N):
            temp += battery[one_route[node_start]][one_route[node_end]]
            if temp > min_v:
                break
            node_start += 1
            node_end += 1
        min_v = min(temp, min_v)    
        
    print('#{} {}'.format(tc, min_v))
