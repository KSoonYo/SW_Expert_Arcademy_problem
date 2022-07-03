import sys

sys.stdin = open('input.txt')


# 인접 리스트와 재귀를 활용한 깊이 우선 탐색
def route(start):
    if start == 99: # 도착지점 발견
        return 1

    # 둘 중에 하나라도 갈 곳이 있는 경우
    # 왼쪽부터 가서 끝 지점까지 내려간다.
    if left[start]:
        left_start = left[start]
        left_return = route(left_start)
        if left_return:
            return 1
    if right[start]:
        right_start = right[start]
        right_return = route(right_start)
        if right_return:
            return 1

    return 0  # 왼쪽 오른쪽에서 경로를 발견하지 못한 경우

result = [0]
for _ in range(10):

    left = [0 for _ in range(100)]
    right = [0 for _ in range(100)]

    tc, edge = map(int, input().split())
    num = list(map(int, input().split()))
    # 입력받은 것을 2개씩 끊어서 요소 튜플화
    tuple_num = []
    idx = 0
    temp = []
    while idx < len(num):
        temp.append(num[idx])
        if len(temp) == 2:
            tuple_temp = (temp[0], temp[1])
            tuple_num.append(tuple_temp)
            temp = []

        idx += 1

    # 요소 정렬
    # 첫번째 요소를 기준으로 오름차순 정렬 후 두번째 요소를 정렬
    tuple_num.sort(key=lambda x: (x[0], x[1]))

    # 도착 지점이 작은 쪽이 left, 큰 쪽이 right
    # 간선이 1개 인 것도 고려
    # tuple_num[0](동일한 시작점)에 대하여 왼쪽 오른쪽 순으로 입력을 받음
    # 간선이 하나인 경우, 왼쪽에만 값 입력
    left[0] = tuple_num[0][1]
    for idx in range(1, len(tuple_num)):
        # 이전 시작점과 동일 시작점인 경우
        if tuple_num[idx][0] == tuple_num[idx-1][0]:
            right[tuple_num[idx][0]] = tuple_num[idx][1]
        else:
            left[tuple_num[idx][0]] = tuple_num[idx][1]

    result.append(route(0)) # 0부터 시작하여 경로가 있는지 탐색

for tc in range(1, 11):
    print('#{} {}'.format(tc, result[tc]))


'''
```python
import sys

sys.stdin = open('input.txt')

def graph(n):
    node = [[] for _ in range(100)] # 갈 수 있는 노드의 숫자만 담기로 했다.
    visit = [False for _ in range(100)] # 방문을 확인하는 노드
    ways = list(map(int, input().split()))
    for i in range(n): # 입력을 노드에 넣는 과정
        node[ways[i*2]].append(ways[i*2 +1])

    def explore(a, g): # a에서 goal을 찾아나가는 여정
        for dest in node[a]: # a가 갈 수 있는 길 dest 중
            if not visit[dest]: #  dest를 가본 적이 없을때
                if dest == g: # dest가 g라면 탐색 성공
                    return 1
                # 그렇지 않으면
                visit[dest] = True # 방문 표시를 한 뒤에
                if explore(dest, g): # dest에서 다시 탐색
                    return 1 # 탐색에 실패하면 return하지 않고, 성공일 경우에만 리턴한다.
                visit[dest] = False # 갔다온 뒤에는 다시 방문표시를 지운다.(이 문제에서는 없어도 될 듯 하다.)

                # 만일 기록이 남아있으면, 다른 노드에서 이 노드로 이어져 있어도 방문 체크 때문에 해당 노드를 방문할 수 없다.
                # 모든 갈림길에서 한번씩 모든 경로를 탐색하며 목적지를 찾으려 한다면 방문했던 곳의 방문기록을 지워줘야 하지만 
                # 이 문제에서는 갈림길이 각 노드마다 최대 2개이며 인접 리스트로 다음 노드를 직접 지정한다는 점
                # 한 갈림길에 이어진 모든 길을 탐색하고 옆 갈림길로 이동하여 이어진 모든 노드를 다시 탐색할 필요가 없이
                # 목적지를 발견하면 곧바로 목적지를 발견했음을 return한다는 점
                # 발견하지 못한 경우, 다른 노드에서 해당 노드로 가봤자 목적지는 나오지 않으므로 다시 방문할 필요가 없다는 점
                # 이러한 사항들 때문에 방문한 기록을 다시 지워주지 않아도 괜찮다.  
        
        return 0

    visit[0] = True
    return explore(0, 99)

for _ in range(10):
    tc, n = map(int, input().split())
    print('#{} {}'.format(tc, graph(n))
```
by 6조 준형님

'''

