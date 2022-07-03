import sys
sys.stdin = open('input.txt')
tests = 10

result = []
for _ in range(tests):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # boxes 돌면서 현재의 최고 박스 높이와 최소 박스 높이를 구한다.
    # dump
    # 덤프 횟수까지 평탄화 작업을 계속함
    work = 0

    # 0811 개선점 발견
    # 반복을 한 번 더 while 문 안에서 해줄 필요 없이 dump+1 로 조건 걸어주면 자동으로 반복을 한 번 더 하게 된다.
    while work < dump:
        min_height = 100
        min_idx = 0
        max_height = 1
        max_idx = 0

        # 현재의 최대 높이와 최소 높이 구하기
        # 전체 길이는 100
        for idx in range(100):
            if boxes[idx] > max_height:
                max_height = boxes[idx]
                max_idx = idx
            if boxes[idx] < min_height:
                min_height = boxes[idx]
                min_idx = idx

        # dump
        boxes[min_idx] += 1
        boxes[max_idx] -= 1
    
        # 한 번 더 반복
        min_height = 100
        min_idx = 0
        max_height = 1
        max_idx = 0

        # 현재의 최대 높이와 최소 높이 구하기
        # 전체 길이는 100
        for idx in range(100):
            if boxes[idx] > max_height:
                max_height = boxes[idx]
                max_idx = idx
            if boxes[idx] < min_height:
                min_height = boxes[idx]
                min_idx = idx
        work += 1

    # 최고점과 최저점의 높이차
    height_difference = max_height - min_height
    result.append(height_difference)

for print_case in range(1, tests + 1):
    print('#{} {}'.format(print_case, result[print_case-1]))

