tests = int(input())

for tc in range(tests):
    sticks = input()
    stack = lazer = result = 0
    # 전략
    # 현재 문자가 ( 인 경우와 ) 인 경우를 각각 고려
    # 현재 문자가 ( 인 경우, stack 에 + 1 적립
    # 현재 문자가 ) 인 경우, 이전 문자가 ( 이면 이는 레이저. => stack 에서 -1 하고 레이저 이전까지의 막대 개수를 result에 더함
    # 현재 문자가 ) 인 경우, 이전문자도 ) 이면 이는 닫히는 경우이므로 stack에서 -1 하고 막대 개수 result에 +1
    # +1 하는 이유? : 어쨌든 막대는 하나 이상의 레이저가 있으므로, 막대가 닫히는 경우 레이저 이후에 막대가 하나 더 생김.
    # 레이저를 기준으로 왼쪽이 막대들을 레이저로 자르고 나서의 막대 개수

    previous = ""
    for char in sticks:
        if char == '(':
            stack += 1
        else:
            if previous == '(':
                stack -= 1
                result += stack
            elif previous == ')':
                result += 1
                stack -= 1
        previous = char
    print("#{} {}".format(tc+1, result))
