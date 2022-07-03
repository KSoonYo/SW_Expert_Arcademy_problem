'''
solution 3조

```python
def babygin(card):
    for j in range(len(card)):
        if card[j] >= 3 :       # triplet 인지 확인
            return 1
    
    if len(card) >= 3:
        for k in range(len(card)-2):     # 인덱스 오류를 고려해서 len(card)-2 로 설정
            if card[k] and card[k+1] and card[k+2]:     # run 인지 확인
                return 1
    return 0

T = int(input())

for tc in range(1,T+1):
    total_cards = list(map(int, input().split()))
    player_a = [0]*10     # [ 0 0 0 0 0 0 0 0 0 0 ]
    player_b = [0]*10     # [ 0 0 0 0 0 0 0 0 0 0 ]
    result = 0

    for i in range(len(total_cards)):
        if i%2 == 0 :
            player_a[total_cards[i]] += 1       # player_a의리스트에 갯수 저장
            if babygin(player_a):
                result = 1           # player a의 승리이므로 1
                break
        else :
            player_b[total_cards[i]] += 1       # player_b의리스트에 갯수 저장
            if babygin(player_b):
                result = 2           # player b의 승리이므로 2
                break
    print('#{} {}'.format(tc, result))
```

'''