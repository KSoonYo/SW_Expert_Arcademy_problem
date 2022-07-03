

for tc in range(1, int(input())+1):
    N = int(input())

    # 5만원, 1만원, 5천원, 1천원, 5백원, 1백원, 5십원, 십원
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_count = [0] * 8

    idx = 0
    while idx < 8:
        if money[idx] > N:
            idx += 1
            continue

        money_count[idx] = N // money[idx]
        N %= money[idx] 
        idx += 1

    print('#{}'.format(tc))
    print(*money_count)
