game_round = int(input())

clab = '-'
three_six_nine = ['3', '6', '9']
for game in range(1, game_round+1):
    count = 0
    string_game = str(game)

    for num in string_game:
        if num in three_six_nine:
            count += 1
    if count > 0:
        print(clab * count, end=' ')
    else:
        print(string_game, end=' ')

