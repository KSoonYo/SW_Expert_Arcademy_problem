
for tc in range(1, int(input())+1):
    N = int(input())
    time_schedule = []
    for _ in range(N):
        wanted_time = tuple(map(int, input().split()))
        time_schedule.append(wanted_time)
    
    # 작업 완료시간을 기준으로 오름차순으로 정렬(작업이 일찍 끝나는 순대로 정렬)
    time_schedule.sort(key=lambda x : x[1])
    selected_time = [time_schedule[0]] # 가장 작업이 일찍 끝나는 화물차 우선 선정

    # 현재 작업이 끝나는 시간과 다음 작업을 시작하는 시간을 비교
    # 다음 작업 시작 시간 >= 현 작업 끝나는 시간 이면 화물차 시간이 겹치지 않는다.

    for idx in range(1, len(time_schedule)):
        next_start_time = time_schedule[idx][0]
        now_finish_time = selected_time[-1][1]
        if next_start_time >= now_finish_time:
            selected_time.append(time_schedule[idx])

    print('#{} {}'.format(tc, len(selected_time)))