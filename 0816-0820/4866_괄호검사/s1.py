
tests = int(input())

def blank(code):
    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            # 주의! stack에 아무것도 없는 상태에서 ) 나 } 를 만났을 때도 고려해줘야 한다.
            if not stack:
                return 0
            last_char = stack[-1]
            if last_char == '(':
                stack.pop()
            else:
                return 0
        elif char == '}':
            if not stack:
                return 0
            last_char = stack[-1]
            if last_char == '{':
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    else:
        return 1


result = [0]
for _ in range(tests):
    code = input().strip()
    stack = []

    result.append(blank(code))


for tc in range(1, tests+1):
    print('#{} {}'.format(tc, result[tc]))

