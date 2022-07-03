# prim을 두번쓰면 쉽게 풀겠는데...
# 우선 bfs로 풀어보자
# runtime error! 젠장!
# => 인접리스트로 하니까 해결!


def bfs(s, e):
    queue = [s]
    distance = [987654321] * (N+1)
    # 시작 위치의 거리는 0
    distance[s] = 0
    front = -1
    rear = 0
    while front != rear:
        front += 1
        start = queue[front]

        # 현재 노드에 인접한 노드들 탐색
        for next, weight in graph[start]:
            if distance[next] > (distance[start] + weight):
                distance[next] = distance[start] + weight
                queue.append(next)
                rear += 1
    return distance[e]


for tc in range(1, int(input())+1):
    # N: 마지막 집의 번호, M: 간선의 개수, X: 도착지점의 번호
    N, M, X = map(int, input().split()) 

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        # 단방향 그래프
        # 인접 리스트로 해볼까
        start, end, weight = map(int, input().split())
        
        graph[start].append((end, weight))

    max_distance = 0
    for s in range(1, N+1):
        go = bfs(s, X)
        back = bfs(X, s)
        max_distance = max(max_distance, go + back)

    print('#{} {}'.format(tc, max_distance))