import sys

sys.stdin = open('input.txt')

tests = int(input())

result = []
for _ in range(tests):
    # 카드의 최대 값만큼의 count_list를 생성
    # 첫번째 카드부터 시작하여 각 카드의 장 수를 count
    # 만약 카드의 값이 0이면 0번째 요소에 +1
    cards_count = int(input())
    cards = input()
    # 0, 1~9 이므로 count할 요소들은 10
    count_list = [0] * 10

    # count
    for card in cards:
        # 카드의 숫자가 0이 아니라면
        if int(card):
            count_list[int(card)] += 1

        # 0이라면
        else:
            count_list[0] += 1

    # 최대 카드 숫자 비교 검사
    top_card_value = count_list[0]
    top_idx = 0
    for card_idx in range(1, len(count_list)):
        if top_card_value < count_list[card_idx]:
            top_card_value = count_list[card_idx]
            top_idx = card_idx
        elif top_card_value == count_list[card_idx]:
            top_idx = card_idx

    result.append((top_idx, top_card_value))

for print_result in range(1, tests+1):
    print('#{} {} {}'.format(print_result, result[print_result-1][0], result[print_result-1][1]))