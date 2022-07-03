
for tc in range(1, int(input())+1):
    # 1일, 1달, 3개월, 1년 요금
    d, m1, m3, y = map(int, input().split())


    plan = [0] + list(map(int, input().split()))

    day_or_month = [0] * 13

    # 각 월에서 1일, 1달, 3개월 치 요금 중 최소 요금을 pick
    # 누적해가면서 dp 완성!

    # 3개월 째부터 시작 하기 위해 1월 2월 치를 미리 dp에 저장
    day_or_month[1] = min(d * plan[1], m1) # 1월의 최소 요금
    day_or_month[2] = day_or_month[1] + min(d * plan[2], m1) # 1월 ~ 2월의 최소요금 / 이전 달 최소 요금 + 이번 달 최소 요금
    
    for month in range(3,13):
        day_or_month[month] = min(day_or_month[month-3] + m3, day_or_month[month-1] + m1, day_or_month[month-1] + (plan[month] * d))



    # 최종적으로 1년 요금과 비교하여 최소 요금을 pick!
    result = min(y, max(day_or_month))

    print('#{} {}'.format(tc, result))

