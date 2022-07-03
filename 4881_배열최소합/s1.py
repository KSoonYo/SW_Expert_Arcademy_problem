

### 다시 풀기

import sys
sys.stdin = open('sample_input.txt')

def get_min(i, s, temp):
    '''
    :param i: 현재의 고려 단계
    :param s: 이전까지의 최소합
    :param temp: 이전까지의 요소 합
    :return: 최소합
    '''

    # i가 N과 같다면(i로 N-1단계까지만 자리 표시 가능)
    # 현재의 node_status 의 요소를 하나씩 돌면서
    # 1인 곳을 만나면 이전 row 의 값이 1이 아닌지 판단 (또는 이전 row 가 영역 밖)
    # 이전 row 의 값이 1이면 num_list 에서 그곳의 인덱스는 쓸 수 없음
    # 이전 row 의 값이 1이 아니면 num_list 에서 그곳의 인덱스를 쓸 수 있음

    # if i == N:
    #     sum_branch = 0
    #     # print('node_status: ', node_status)
    #     for row in range(len(node_status)):
    #         for column in range(len(node_status[0])):
    #             if sum_branch > min_s:
    #                 return None
    #             if node_status[row][column] == 1:
    #                 if row-1 < 0 or node_status[row-1][column] != 1:
    #                     sum_branch += num_list[row][column]
    #                     # print('num_list:', num_list[row][column])
    #                 else:
    #                     continue
    #     # 배열 루트 하나의 합
    #     # print('sum_branch:', sum_branch)
    #     return sum_branch

    # [0,0,0....]
    # 같은 메모리 주소를 가리키고 있으므로 current_level 값을 변경하면 자동으로 노드 스테이터스도 변경된다.
    current_level = node_status[i]
    candidate = []

    if i > 0:
        previous_level = node_status[i - 1]
        # 이전 단계의 인덱스 위치를 검사하여 1인 곳을 현재 단계에서도 check
        # 나머지 1이 아닌 곳이 현재 단계에서 갈 수 있는 후보군
        for idx in range(len(previous_level)):
            if previous_level[idx] == 1:
                current_level[idx] = 1

        for candidate_idx in range(len(current_level)):
            if current_level[candidate_idx] != 1:
                current_level[candidate_idx] = 1
                candidate.append(current_level[:])
                current_level[candidate_idx] = 0


    else:
        # i = 0 단계에서는 현재 단계의 모든 자리가 후보군
        for idx in range(len(current_level)):
            current_level[idx] = 1
            candidate.append(current_level[:])
            current_level[idx] = 0

    # print('current_level:', i, 'current_candidate: ', candidate)

    
    # 최소값 초기화
    min_s = s

    # 지금 단계에서 갈 수 있는 각각의 후보군을 돌면서
    # 후보군에 해당하는 node_status 값을 변경시켜주고
    # i += 1 씩 증가시켜 아래 단계로 내려감

    temp_sum = temp
    column = 0
    for level in candidate:
        node_status[i] = level
        # print('now_node_status: ', node_status[i])
        # print('temp_sum:', temp_sum)
        # print('current_level:', i, 'current_level ', level)

        # 현재 단계의 위치에서 오는 값을 temp_sum에 누적
        # 현재 단계의 위치 값은 같은 열의 이전 row가 영역 밖이거나 0이면 현재 단계로 오는 위치값
        for col in range(len(level)):
            if node_status[i][col] == 1 and (i-1 < 0 or node_status[i-1][col] != 1):
                temp_sum += num_list[i][col]
                column = col
                # print('temp_sum추가', num_list[i][col])

        # temp_sum이 만약 현재의 최소값보다 크다면
        # 더 이상 다음 레벨로 내려가 탐색할 필요 없이 다음 후보군으로 skip
        if temp_sum > min_s:
            temp_sum -= num_list[i][column]
            continue

        else:
            # 다음 레벨 단계 고려
            # 고려하기 전에 청소
            if i < N and i + 1 < N:
                node_status[i + 1] = [0] * N
                min_s = get_min(i + 1, min_s, temp_sum)

            # 마지막 단계까지 내려갔다면
            # 최소값 업데이트
            if i + 1 == N and min_s > temp_sum:
                min_s = temp_sum
                # print('temp sum2 : ', temp_sum)
        # 최소값 BACK
        temp_sum -= num_list[i][column]
    return min_s

# 최초 초기값 구하는 함수


def get_init_min(num_list):
    result = 0
    for row in range(len(num_list)):
        # 대각선 값만 구함
        result += num_list[row][row]

    return result


tests = int(input())
for tc in range(1, tests+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    node_status = [[0 for i in range(N)] for j in range(N)]
    min_s = get_init_min(num_list)
    ans = get_min(0, min_s, 0)
    print('#{} {}'.format(tc, ans))




'''
조금 더 쉬운 solution)


import sys
sys.stdin = open('input.txt')

def dfs(current, sum_val):
    """
    dfs 함수
    현재 위치와 현재까지의 sum_val를 입력
    행과 열을 탐색하며 min_value를 업데이트
    """
    # 본문에서 선언된 변수 global 사용
    global min_value
    # 현재위치가 마지막 열일 경우, sum 값과 min 값을 비교 & 업데이트
    if current == N:
        if min_value > sum_val:
            min_value = sum_val
            return
    # 현재위치가 마지막 열에 도달하지 못했는데 이미 min 값을 넘었다면, 업데이트 X
    if sum_val >= min_value:
        return
    # 열을 탐색하며, 안에서 현재위치를 변화시키며 탐색
    for i in range(N):
        # 탐색 한 세로줄은 다시 탐색할 수 없음
        if visited[i]:
            visited[i] = False
            dfs(current+1, sum_val+number_arr[current][i])
            # 재탐색을 위한 초기화
            visited[i] = True

T = int(input())

for t in range(1, T+1):
    N = int(input())
    number_arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 위치를 True로 기본 설정.
		visited = [True for _ in range(N)]

		# 각 자리별로 들어갈 수 있는 최대의 값은 9 이므로 
		# N만큼 곱하게 되면 얻을 수 있는 최대의 값이 된다.
    min_value = 9*N
		# 현재위치 변수 및 현재 합산 값 변수 선언
    Current = 0
    Sum_value = 0
    dfs(Current, Sum_value)
    print('#{0} {1}'.format(t, min_value))

'''


