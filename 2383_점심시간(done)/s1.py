import sys

sys.stdin = open('sample_input.txt')



def move(a_list, b_list):
    global min_time    
    time = 1 # 전체 시간, 계단과 사람 위치는 겹쳐지지 않으므로 모든 경우에 사람은 게단에 도착하기까지 최소 1분이 걸린다.

    # A 계단 
    a_stair = stairs[0]

    # B 계단
    b_stair = stairs[1]

    # 각 그룹의 구성원이 계단으로 이동하는데 걸리는 시간
    to_a_distacne = []
    to_b_distance = []
    for a_person in a_list:
        to_a_distacne.append(abs(a_person[0] - a_stair[0]) + abs(a_person[1] - a_stair[1]))
    
    for b_person in b_list:
        to_b_distance.append(abs(b_person[0] - b_stair[0]) + abs(b_person[1] - b_stair[1]))

    # 오름차순으로 정렬
    to_a_distacne.sort()
    to_b_distance.sort()

    a_queue = [] # 계단 입구 대기자
    b_queue = []

    a_down = [] # 계단을 내려가고 있는 사람들 리스트
    b_down = []

    while to_a_distacne or a_queue or a_down or to_b_distance or b_queue or b_down:
        
        # print('####')
        # print('time:', time)

        if time > min_time:
            return
        # print('a_distance', to_a_distacne)
        if to_a_distacne:
            # 계단 입구 도착
            # 현재 time에 계단 입구에 도착한 사람을 골라서 대기자 명단으로 이동시킴
            a_cnt = 0
            for a_arrive in to_a_distacne:
                if a_arrive == time:
                    # print(time,'분 a 계단에 사람 도착!')
                    a_queue.append(a_arrive)
                    a_cnt += 1
            # 리스트 갱신
            for _ in range(a_cnt):
                to_a_distacne.pop(0)

        # print('b_distance', to_b_distance)
        if to_b_distance:
            b_cnt = 0
            for b_arrive in to_b_distance:
                if b_arrive == time:
                    # print(time,'분 b 계단에 사람 도착!')
                    b_queue.append(b_arrive)
                    b_cnt += 1
            for _ in range(b_cnt):
                to_b_distance.pop(0)

        # 계단 입구 대기자 중 도착한지 1분이상 지났다면 pop해서 계단으로 내려보낸다.
        # 계단에 이미 세 명의 사람이 있다면 계단의 자리가 빌 때까지 대기한다.
        
        a_front = a_queue[0] if a_queue else 0
        b_front = b_queue[0] if b_queue else 0

        a_full = b_full = False
        if a_front and time > a_front:
            a_cnt = 0
            for waiting_person in a_queue:
                if a_front == waiting_person and len(a_down) < 3:
                    a_down.append(waiting_person + (time - waiting_person))
                    a_cnt += 1
                    # print(time, '분에 a계단을 내려감!')

            for _ in range(a_cnt):
                a_queue.pop(0)        

            if len(a_down) == 3:
                a_full = True
            
        if b_front and time > b_front:
            b_cnt = 0
            for waiting_person in b_queue:
                if b_front == waiting_person and len(b_down) < 3:
                    b_down.append(waiting_person + (time - waiting_person))
                    # print(time, '분에 b계단을 내려감!')
                    b_cnt += 1
            
            for _ in range(b_cnt):
                b_queue.pop(0)

            if len(b_down) == 3:
                b_full = True

        # print('a_queue', a_queue)
        # print('b_queue', b_queue)

        # 계단을 내려간다.
        # 걸리는 시간은 계단의 길이만큼! a_stair[2], b_stair[2]
        a_first = a_down[0] if a_down else None
        b_first = b_down[0] if b_down else None

        if a_first and time == a_first + a_stair[2]:
            # 계단을 모두 내려갔다면
            a_cnt = 0
            for in_stair_person in a_down:
                if in_stair_person == a_first:
                    # 도착! 
                    a_cnt += 1
                    # print(time, '분에 한 사람 a 게단 내려옴')
            for _ in range(a_cnt):
                a_down.pop(0)
                if a_full and a_queue and time > a_queue[0]:
                    # 계단에 있는 3명의 사람 중 1명의 사람이 나가면, 나가자마자 대기자 명단에 있는 사람을 계단에 들어오도록 할 수 있음            
                    a_queue.pop(0)
                    a_down.append(time)

        if b_first and time == b_first + b_stair[2]:
            # 계단을 모두 내려갔다면
            b_cnt = 0
            for in_stair_person in b_down:
                if in_stair_person == b_first:
                    # 도착!
                    b_cnt += 1
                    # print(time, '분에 한 사람 b 계단 내려옴')
            for _ in range(b_cnt):
                b_down.pop(0)
                if b_full and b_queue and time > b_queue[0]:
                    b_queue.pop(0)
                    b_down.append(time)

        # print('a_down', a_down)
        # print('b_down', b_down)

        time += 1

    min_time = min(min_time, time-1)
    return



def grouping(idx, k):
    '''
    idx는 선택된 사람,
    k명의 사람을 a_group에 append
    '''
    a_group.append(people[idx])
    
    if len(a_group) == k:
        # print('a_group', a_group)
        # b grouping
        b_group = []
        for person in people:
            if person not in a_group:
                b_group.append(person)
        # print('b_group', b_group)
        move(a_group, b_group)
        return


    for another_idx in range(idx+1, len(people)):
        grouping(another_idx, k)
        a_group.pop()
        

for tc in range(1, int(input())+1):

    '''
    핵심전략
    1) A그룹과 B그룹을 나눈다.(1번째 계단과 2번째 계단을 사용할 집단을 조합으로 구함)

    2) 각각의 그룹에서 계단으로 움직이는 집단, 계단 입구에서 대기하는 집단, 계단을 내려가는 집단 으로 분류하고    

    3) 누군가 계단에 도착한 경우, 계단 입구에서 대기하는 집단으로 이동
    
    4) 최소 1분 이상 대기한 뒤 계단 안에 사람이 3명 이하면 계단을 내려가는 집단으로 이동
    (이때, 계단을 내려가는 사람은 자기가 계단에 도착한 시간 + 추가로 대기한 시간 정보를 가지고 있어야 한다.)
    
    5) 자기가 가지고 있는 시간 정보에서 계단의 길이만큼의 시간을 더하면 계단을 모두 내려온 것으로 간주
    
    6) 계단 안에 3명인 상태에서 한 사람이 계단을 모두 내려왔다면, 
    곧바로 다음 사람(그러나 현재 시간이 다음 사람이 도착한 시간보다 최소 1이상 커야함)이 계단을 내려가는 집단으로 이동

    7) 계단으로 이동하는 사람, 대기자, 계단을 내려가는 사람 모두 비어있으면(a,b그룹 모두) 전원 계단 내려가기 완료!    
    '''
    N = int(input())

    map_info = [list(map(int, input().split())) for _ in range(N)]

    stairs = []
    people = []
    
    # 계단 좌표 길이 탐색
    # 사람들의 좌표 탐색
    for row in range(N):
        for col in range(N):
            if map_info[row][col] > 1:
                stairs.append((row, col, map_info[row][col]))

            elif map_info[row][col] == 1:
                people.append([row, col])

    
    # 아무도 A 계단을 이용하지 않을 때
    # 한 사람만 A 계단을 이용할 때
    # 두 사람만 A 계단을 이용할 때
    # 세 사람만 A계단을 이용할 때
    # ...
    # 나머지는 모두 B계단 이용 
    # print('people', people)

    min_time = 987654321
    k = 0
    while k <= len(people):
        if k == 0: # 아무도 A계단을 이용하지 않을 때
            b_group = people[:]
            move([], b_group)
        elif k == len(people): # 모든 사람들이 A계단을 이용할 때
            a_group = people[:]
            move(a_group, [])
        else:
            for idx in range(len(people)):
                a_group = []
                grouping(idx, k) # k명의 사람이 A계단을 이용할 때 인원 조합
        k += 1
    print('#{} {}'.format(tc, min_time))