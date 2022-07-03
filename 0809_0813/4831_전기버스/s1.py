# # k: 버스 최대 이동 가능 거리
# # n: 종점
# # m 충전기 갯수
# # 충전기 위치 표시
import sys
sys.stdin = open('input.txt')

def Bus(k, n, m, charge_location):
    charge_loc_list = [0] * (n + 1)

    for idx in range(m):
        charge_loc_list[charge_location[idx]] += 1

    # 충전을 하면 movement는 0으로 초기화
    # 충전을 하면 charge + 1, 충전한 위치에서 다음 이동 범위 내 충전소 선택

    # 만약 이동 범위 내 충전을 하지 못하면 0 출력
    # 총 이동 거리가 n을 넘으면 charge 값 출력

    charge = 0

    start_movement = 0
    last_charge = 0

    while True:
        movement = 1
        charge_change = 0

        # 현재 위치에서 이동 범위 내 충전소 중 가장 나중에 있는 것 선택
        while movement <= k:
            start_movement += 1
            if start_movement < n and charge_loc_list[start_movement]:
                charge_change += 1
                last_charge = start_movement

            movement += 1

            if start_movement >= n:
                charge_change = 0

        if not charge_change:
            break

        else:
            start_movement = last_charge
            charge += 1

    if start_movement >= n:
        return charge
    else:
        return 0


test_cases = int(input())

result_list = []

for case in range(1, test_cases + 1):
    k, n, m = map(int, input().split())
    charge_location = list(map(int, input().split()))
    result_list.append(Bus(k, n, m, charge_location))

for print_case in range(1, test_cases + 1):
    print('#{} {}'.format(print_case, result_list[print_case - 1]))

