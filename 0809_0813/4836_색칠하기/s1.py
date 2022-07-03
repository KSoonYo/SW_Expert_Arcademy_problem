# # import sys

# # sys.stdin = open('input.txt')

# tests = int(input())

# def coloring(purple_area, red_area, blue_area):
#     count_purple = 0
#     for row in range(len(red_area)):
#         for column in range(len(red_area[0])):
#             if not purple[row][column] and red_area[row][column] == blue_area[row][column]:
#                 purple_area[row][column] = 1
#                 count_purple += 1
#     return count_purple


# for _ in range(tests):
#     area_complex = int(input())

#     # 영역 그리기
#     red_list = []
#     blue_list = []
    
#     for _ in range(area_complex):
#         red = [1]
#         blue = [2]
#         area = list(map(int, input().split()))
#         color = area[-1]
#         # 왼쪽 두 개가 시작점, 오른쪽 두 개가 종착점
#         # n x m
#         n = area[3] - area[1] + 1 
#         m = area[2] - area[0] + 1
        
#         if color == 1:
#             red = [[(i,j) for j in range(m)] for i in range(n)] 
#             red_list.append(red)
#         else:
#             blue = [[(i,j) for j in range(m)] for i in range(n)]
#             blue_list.append(blue)
        
#     # 영역검사 후 겹치는 부분이 있으면 해당 요소의 값을 비교
#     # 이 때 이미 보라색으로 칠한 경우는 더하지 않음
    
#     # 보라색 영역
#     purple = [[0 for _ in range(len(red_list[0][0]))] for _ in range(len(red_list[0]))]
#     count_purple = 0

#     idx = 0
#     red_idx = 0
#     blue_idx = 0
#     while True:
#         if len(red_list) > len(blue_list):
#             count_purple += coloring(purple, red_area=red_list[red_idx], blue_area=blue_list[blue_idx])


import sys

sys.stdin = open('sample_input.txt')

tests = int(input())


result = [0]
for _ in range(tests):
    area_complex = int(input())

    # 영역 그리기
    colored_area = [[0 for _ in range(10)] for _ in range(10)]
    purple_count = 0

    for _ in range(area_complex):
        red = [1]
        blue = [2]
        area = list(map(int, input().split()))
        color = area[-1]
        # 왼쪽 두 개가 시작점, 오른쪽 두 개가 종착점
        
        # color 1 : red, color 2: blue
        
    # 전체 격자 무늬를 돌면서 영역 내에 정해진 색깔로 영역 색칠
    # 만약 다른 색깔을 만나면 purple로 칠하고 +1
    # 이미 purple이 색칠되어 있거나 동일한 색깔을 만나면 칠하지 않음

        for row in range(10):
            for col in range(10):
                # for문 range 부분을 잘 조정해주면 영역을 굳이 조건문을 걸지 않아도 된다.
                if area[0] <= row <= area[2] and area[1] <= col <= area[3]:
                    if not colored_area[row][col] and color == 1:
                        colored_area[row][col] = 'red'
                    elif not colored_area[row][col] and color == 2:
                        colored_area[row][col] = 'blue'
                    elif (color == 1 and colored_area[row][col] == 'blue') or (color == 2 and colored_area[row][col] == 'red'):
                        colored_area[row][col] = 'purple' 
                        purple_count += 1
    
    result.append(purple_count)




for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))