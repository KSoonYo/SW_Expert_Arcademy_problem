def dfs(start, end, cnt=0):
    global max_distance

    # 현재 노드 방문처리
    visit[start] = 1
    cnt += 1

    if start == end:
        max_distance = max(max_distance, cnt)
        return 

    # 현재 노드와 인접한 노드들 중 방문 가능한 노드 탐색
    for next_node in range(1, N+1):
        # 인접해있고 다음 노드에 방문한 적이 없으면
        if graph[start][next_node] and (not visit[next_node]): 
            dfs(next_node, end, cnt)
            visit[next_node] = 0



for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # 정점 갯수, 간선 정보
    
    # 그래프 입력받기
    graph = [[0] * (N+1) for _ in range(N+1)]

    for edge in range(M):
        node1, node2 = map(int, input().split())
        graph[node1][node2] = 1
        graph[node2][node1] = 1


    max_distance = 0
    
    for start in range(1, N+1):
        for end in range(1, N+1):
            visit = [0] * (N+1)
            dfs(start, end)

    print('#{} {}'.format(tc, max_distance))

