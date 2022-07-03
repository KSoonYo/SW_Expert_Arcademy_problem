import sys

sys.stdin = open('sample_input.txt')

tests = int(input())

# 승자를 가리는 함수
def game(arr, player1, player2):
    '''
    :param arr: 카드 리스트
    :param player1: player1의 번호
    :param player2: player2의 번호
    :return: winner의 번호
    '''
    # print('player1: ', player1)
    # print('player2: ', player2)
    # player1의 카드 번호
    player1_card = arr[player1]
    # player2의 카드 번호
    player2_card = arr[player2]

    # (왼쪽 플레이어 기준)
    # 1: 가위는 [1,3] win, [1,1] draw [1, 2] lose
    # 2: 바위는 [2,1] win, [2,2] draw, [2,3] lose
    # 3: 보는 [3, 2] win [3,3] draw, [3,1] lose

    # win과 lose에 없는 패턴은 모두 무승부
    game_rule = {
        'win': [[1,3], [2,1], [3,2]],
        'lose': [[1,2], [2,3], [3,1]]
    }

    # 왼쪽 플레이어가 이기면 오른쪽 플레이어는 패배
    # 왼쪽 플레이어가 지면 오른쪽 플레이어는 승리
    # 왼쪽 플레이어와 오른쪽 플레이어 모두 카드번호가 같으면 무승부 => 작은 번호의 플레이어가 승리

    now_pattern = [player1_card, player2_card]
    if now_pattern in game_rule['win']:
        # player1 승리
        return player1
    elif now_pattern in game_rule['lose']:
        # player2 승리
        return player2
    else:
        # 무승부인 경우
        if player1 < player2:
            return player1
        else:
            return player2

# 좌,우로 학생 그룹 나누기
def div_groups(cards_list, start, end):
    '''
    :param cards_list: 카드 배열
    :param start: 구간 시작지점
    :param end: 구간 끝지점
    :return: winner의 번호
    '''

    sub_list = []
    for idx in range(start, end+1):
        sub_list.append(idx)

    # 개선점
    # start == end 일 때를 조건으로 걸어서 return 해도 될 듯 => 굳이 sub_list를 만들 필요가 없음
    if len(sub_list) == 1:
        return sub_list[0]

    middle = (start+end) // 2

    # 왼쪽 오른쪽 구간을 나누고

    left_group = div_groups(cards_list, start, middle)
    right_group = div_groups(cards_list, middle+1, end)


    # 각 구간의 승자 가리기
    winner = game(cards_list, left_group, right_group)
    # print('winner: ', winner+1)
    # 가장 마지막 함수에서 최종 승자 return
    return winner


for tc in range(1, tests+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # div_groups 함수에서 반환되는 값은 index이므로 학생 번호를 찾으려면 +1 해야 함.
    print('#{} {}'.format(tc, div_groups(cards, 0, len(cards)-1) + 1))
