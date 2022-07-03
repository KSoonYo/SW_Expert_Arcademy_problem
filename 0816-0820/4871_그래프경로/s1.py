
tests = int(input())


# 간선 연결한 노드 그래프를 따라 완전 탐색
# 만약 방문 경로에 도착 노드가 있다면 return 1(경로 존재)
# 출발지에서 시작하여 갈 수 있는 모든 노드를 방문했음에도 도착 노드가 나오지 않는다면 return 0
def dfs(start, end):
    visited = [0 for _ in range(len(nodes[0]))] # 방문 체크 리스트
    node_stack = [] # 방문 경로(노드) 기록 리스트
    visited[start] = 1
    i = start # 시작 노드
    while i != 0:
        if i == end: # 현재 방문한 노드가 도착지라면
            return 1
        for w in range(1, len(nodes[0])): # next_nodes 의 첫 요소부터 다음 방문할 노드 탐색
            if nodes[i][w] == 1 and visited[w] == 0:
                # 방문할 노드가 있다면 현재 노드는 stack에 push
                node_stack.append(i)
                visited[w] = 1 # 방문 표시
                i = w
                break
        else: # 더 이상 방문할 노드가 없을 경우
            if node_stack: # 이전 방문한 경로로 되돌아가기
                i = node_stack.pop()
            else: # 돌아갈 방문 경로가 없다면 탐색 종료
                i = 0

    return 0 # start 노드부터 시작하여 갈 수 있는 모든 노드를 방문했음에도 목적지 노드를 방문하지 못한 경우


result = [0]
for _ in range(tests):
    v, e = map(int, input().split()) # 정점 개수 v와 간선 개수 e
    nodes = [[0 for i in range(v+1)] for j in range(v+1)] # 노드
    # 간선 연결 작업
    # 단방향으로만 간선 연결
    for edge in range(e):
        node1, node2 = map(int, input().split())
        nodes[node1][node2] = 1
    # 출발 노드와 도착 노드
    start, end = map(int, input().split())
    result.append(dfs(start, end))

for tc in range(1, tests+1):
    print('#{} {}'.format(tc, result[tc]))
