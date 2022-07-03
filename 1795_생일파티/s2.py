'''
prim 2번도 런타임이 걸린다.
아무래도 연결된 노드 수가 엄청 많아질 때 인접행렬로 하면
연결 여부와 상관없이 전부 탐색하므로 시간이 오래걸리는 듯

'''


def prim(s, e):
    key = [987654321] * (N+1)
    key[s] = 0 # 시작점 처리, 시작점의 거리는 0
    visited = [0] * (N+1)

    for _ in range(N):
        minV = 987654321
        min_index = 0
        
        # 방문하지 않은 노드들 중 최소 가중치 노드 선택
        for i in range(1, N+1):
            if not visited[i] and minV > key[i]:
                minV = key[i]
                min_index = i

        visited[min_index] = 1
        
        if visited[e]:
            return key[e]

        # 가중치 갱신
        # 거리 누적으로!
        # 방문처리한 노드와 인접한 노드들 중에서 방문하지 않은 노드들
        for j in range(1, N+1):
            if graph[min_index][j] and not visited[j]:
                if key[j] > key[min_index] + graph[min_index][j]:
                    key[j] = key[min_index] + graph[min_index][j]

for tc in range(1, int(input())+1):
    # N: 마지막 집의 번호, M: 간선의 개수, X: 도착지점의 번호
    N, M, X = map(int, input().split()) 

    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        # 단방향 그래프
        start, end, weight = map(int, input().split())
        graph[start][end] = weight

    max_distance = 0
    for s in range(1, N+1):
        go = prim(s, X)
        back = prim(X, s)
        max_distance = max(max_distance, go + back)

    print('#{} {}'.format(tc, max_distance))