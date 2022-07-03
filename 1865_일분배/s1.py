import sys

sys.stdin = open('input.txt')

def get_max(row, temp, max_value, works):
    
    if temp <= max_value:
        return max_value

    if row > N:
        return max(temp, max_value)

    # 현재의 노동자가 선택 할 수 있는 노동들
    next_works = []
    for next_work in range(1, N+1):
        if next_work not in works:
            next_works.append(next_work)

    for next in next_works:
        now_possibility = temp * possibility_table[row][next] / 100
        works.append(next)
        max_value = get_max(row+1, now_possibility, max_value, works)
        works.pop()

    return max_value
    



for tc in range(1, int(input())+1):
    N = int(input())

    # 성공 확률표 입력받기
    # 1부터 확률표 시작
    possibility_table = [[0] * (N+1)] + [ [0] + list(map(int, input().split())) for _ in range(N)]
    
    # 최대값 초기화
    max_value = 0
    works = []
    result = get_max(1, 1, max_value, works) * 100
    print('#{} {:6f}'.format(tc, result))
