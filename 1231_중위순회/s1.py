import sys

sys.stdin = open('input.txt')

# 문자열 정수를 정수형으로 형변환하는 함수
# '1' -> 1
def to_int(input_string):
    if input_string.isdigit():
        input_string = int(input_string)
    return input_string

# 입력 데이터를 부모, 데이터, 자식 노드들로 분리해주는 함수
def trim(p, d, c1=None, c2=None):
    parent = p
    data = d
    left_child = c1
    right_child = c2

    return parent, data, left_child, right_child

# 트리 중위순회
def in_order(t, s=''):
    # t: 현재 노드
    # s: 문자열 합
    if t:
        # 왼쪽 자식 노드 탐색
        s += in_order(left[t])
        # 현재 노드의 문자열을 결합
        s += node_data[t]
        # 오른쪽 자식 노드 탐색
        s += in_order(right[t])
    return s



for tc in range(1, 11):
    # N : 정점의 총 개수
    N = int(input())

    # 왼쪽 자식 리스트, 오른쪽 자식 리스트
    # 인덱스는 부모 정점의 번호
    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N + 1)]

    # 부모 노드에 들어있는 데이터 관리
    node_data = [0 for _ in range(N + 1)]

    # 트리 입력받기
    for _ in range(N):
        # 입력 데이터
        # data 를 제외한 나머지는 모두 정수형으로 형변환
        # parent, data, left_child, right_child
        input_data = list(map(to_int, input().split()))

        parent, data, left_child, right_child = trim(*input_data)

        # 부모 노드 정점에 data 입력
        node_data[parent] = data

        # tree 구성 (부모 노드가 자식 노드 번호를 가리킴)
        if left_child:
            left[parent] = left_child
        if right_child:
            right[parent] = right_child

    # 노드는 1부터 시작
    print('#{}'.format(tc), in_order(1))
