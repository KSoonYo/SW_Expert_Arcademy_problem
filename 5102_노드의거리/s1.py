# 너비 우선 탐색 문제
import sys
sys.stdin = open('sample_input.txt')


def bfs(s, g, adj):
    visited = [0] * (v+1) # 방문지 리스트
    queue = []  # 큐 생성

    # 첫 시작점 큐에 추가
    queue.append(s)
    visited[s] = 1 # 첫 시작 방문 처리

    # 현재 위치에서 방문 가능한 곳을 탐색하여 queue에 저장
    while queue: # 큐가 빌 때까지 반복
        t = queue.pop(0)
        if t == g:
            return visited[t] - 1
        for w in adj[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1

    # 방문할 수 있는 지점 모두 돌았는데도 목적지가 나오지 않으면?
    # 목적지는 갈 수 없는 곳! (문제에서 간선이 없는 경우도 있다고 했음)
    return 0


tests = int(input())
for tc in range(1, tests+1):
    # 노드 개수: v, 방향성이 없는 간선 e의 개수
    # 방향성이 없음 -> 양방향
    v, e = map(int, input().split())

    # 인접 리스트 활용
    # 노드 개수만큼
    adj_list = [[] for _ in range(v+1)]

    for _ in range(e):
        s1, s2 = map(int, input().split())
        # print(start, '->', end)
        adj_list[s1].append(s2)
        adj_list[s2].append(s1)

    # s는 시작지점, g는 목적지
    s, g = map(int, input().split())
    ans = bfs(s,g,adj_list)
    print('#{} {}'.format(tc, ans))


'''

다음 레벨로 넘어가는 걸 재귀 없이 반복으로 구현하는 방법. 
solution)

by 6조

import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')
t = int(input())

for test_case in range(1, t + 1):
    v, e = map(int, input().split())
    adjacency_list = [[] for _ in range(v + 1)]  # 인덱스 맞추기 위해 +1
    queue_level = [[] for _ in range(v)]
		# level = 0 을 start 지점으로 생각하고, start 에 연결되어 있는 노드들이 level = 1 이 되어 queue_level[1]에 저장된다.
		# test_case 1번의 경우 나중에 while문을 돌면서 [[1], [4, 3], [2, 6]] 형태로 저장될 것
    visited = [False] * (v + 1)

		# 인접리스트 생성
    for i in range(e):
        v1, v2 = map(int, input().split())
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)

    start, end = map(int, input().split())
    level = 0 # level을 0으로 초기화하고 시작
    queue_level[level].append(start) # start 지점은 level 0으로 queue_level[0]에 넣고 시작

    while queue_level[level]:
				# 현재 level에 있는 리스트의 값을 pop해서 가져온다. 
        current_node = queue_level[level].pop()

				# 도착지점에 도달한 경우 result 에 level을 할당하고 종료
        if current_node == end:
            result = level
            break

				# 방문 처리
        visited[current_node] = True

				# 인접리스트에 있는 노드중 방문하지 않은 노드를 queue_level의 level + 1에 저장한다.
        for adjacent_node in adjacency_list[current_node]:
            if not visited[adjacent_node]:
                queue_level[level + 1].append(adjacent_node)

				# 현재 level에 해당하는 리스트에 값이 없으면 level + 1하고 while 문을 다시 순회한다.
        if not queue_level[level]:
            level += 1

    else:
				# break문으로 빠져나가지 않고 while문이 끝났으므로 경로가 없다는 의미이므로 결과로 0을 할당한다.
        result = 0

    print('#{} {}'.format(test_case, result)

'''

