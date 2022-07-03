import sys

sys.stdin = open('sample_input.txt')


direction_dict = {
    1 : lambda x : x - 1,                                               # 상
    2 : lambda x : x + 1,                                               # 하
    3 : lambda y : y - 1,                                               # 좌
    4 : lambda y : y + 1                                                # 우
}


def unify(row, col, group, cluster):
    unified_individual = [row, col, 0, 0]
    maxV = 0
    for member in group:
        unified_individual[2] += member[2]
        if member[2] > maxV:
            maxV = member[2]
            unified_individual[3] = member[3]

    zone[row][col] = [unified_individual]
    remove_items_idx = []                                               # (row, col)에 모인 기존 군집들 모두 제거
    for prev_individual in cluster:                                     
        if (prev_individual[0], prev_individual[1]) == (row, col):
            remove_items_idx.append(cluster.index(prev_individual))

    new_cluster = []
    for cluster_idx in range(len(cluster)):
        if cluster_idx not in remove_items_idx:
            new_cluster.append(cluster[cluster_idx])

    new_cluster.append(unified_individual)                                  # 새로 통합된 개체를 군집 정보에 append
    return new_cluster


def collision(row, col, crashed_individual, cluster):
    '''
    현재 있는 미생물 수 // 2
    방향 반대로 전환
    '''
    prev_idx = cluster.index(crashed_individual)                        # 군집 리스트에서 충돌한 개체군집의 인덱스 추출
    new_individual = cluster.pop(prev_idx)                              # 충돌한 개체군집 추출
    new_individual[2] = crashed_individual[2] // 2                      # 현재 미생물 수 반으로 줄이기

    if not new_individual[2]:                                           # 군집이 모두 죽었다면 그대로 함수 종료
        return cluster

    if crashed_individual[3] == 1:
        new_individual[3] = 2
    elif crashed_individual[3] == 2:
        new_individual[3] = 1
    elif crashed_individual[3] == 3:
        new_individual[3] = 4
    elif crashed_individual[3] == 4:
        new_individual[3] = 3
    
    cluster.append(new_individual)                                      # 군집 정보 갱신

    zone[row][col].append(new_individual)                               # 지도 정보 갱신

    return cluster

def move(M, cluster):
    '''
    M: 최대 시간(최대 움직이는 횟수)
    cluster : 군집 정보
    '''

    if M == 0:                                                          # 이동이 끝났을 때, 남아있는 미생물 수 반환
        result = 0
        for individual in cluster:
            result += individual[2]
        return result


    for individual in cluster:                                          # 이동
        individual_direction = individual[3]
        zone[individual[0]][individual[1]].pop(0)                       # 이동 전 현재 위치에 있는 군집 pop(0) : zone 요소들이 모두 queue
        
        if individual_direction == 1 or individual_direction == 2:      # 방향이 상, 하라면
            individual[0] = direction_dict[individual_direction](individual[0])

        else:                                                           # 방향이 좌, 우라면
            individual[1] = direction_dict[individual_direction](individual[1])
            
        zone[individual[0]][individual[1]].append(individual)           # 이동 후 현재 위치에 군집 append
        

    for row in range(N):
        for col in range(N):
            if row == 0 or row == N-1:                                  # 위쪽 또는 아래쪽 벽에 충돌했을 때
                if zone[row][col]:                                      # 해당 위치로 이동한 군집이 있다면
                    cluster = collision(row, col, zone[row][col].pop(0), cluster)   # cluster scope 조심!
            
            elif col == 0 or col == N-1:                                # 왼족 또는 오른쪽 벽에 충돌했을 때
                if zone[row][col]:      
                    cluster = collision(row, col, zone[row][col].pop(0), cluster)

            elif len(zone[row][col]) > 1:                               # 현재 위치에 군집이 2개 이상 있는 경우
                cluster = unify(row, col, zone[row][col], cluster)      # 통합

    
    return move(M-1, cluster)                                           # 다음 이동





for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())                                 # N: 변의 길이, M: 격리 시간, k : 군집 개수

    cluster = []                                                        # 군집 정보 리스트
    for _ in range(K):
        cluster.append(list(map(int, input().split())))                 # [세로 위치, 가로 위치, 미생물 수, 방햘(1 상, 2 하, 3 좌, 4 우)]


    zone = [[[] for _ in range(N)] for _ in range(N)]                   # zone 설정,  첫 행, 마지막 행, 첫 열, 마지막 열은 벽 

    for individual in cluster:                                          # 초기 위치 setting
        zone[individual[0]][individual[1]].append(individual)           # individual[0] 세로 위치(행), [1] 가로 위치(열)
    

    ans = move(M, cluster)                                              # 이동 시작!
    print('#{} {}'.format(tc, ans))


'''
1207 TIL

list scope를 조심하자!
list가 참조변수이긴 하지만 함수 인자로 들어왔을 함수 내부에서 리스트를 업데이트 했더라도 함수 바깥에 있는 리스트는 업데이트가 반영이 안될 수 있음!

따라서 리스트를 아예 인자로 받지 않거나, 
리스트가 인자로 들어왔다면 함수 동작 중 리스트 내부 변경사항 발생 시 계속 재할당을 해주면서 업데이트를 해줘야 한다.

'''

