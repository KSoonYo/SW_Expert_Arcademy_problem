
tests = int(input())

result = [0]
for _ in range(tests):
    string = input()
    # 문자들을 만날 때마다 stack에 push
    # 근데 가장 최근에 저장한 문자와 새로 만난 문자가 같으면? pop
    # 남은 stack 원소 개수 return
    stack = []
    char_idx = 0
    while char_idx < len(string):
        if char_idx == 0:
            stack.append(string[char_idx])
            char_idx += 1

        else:
            # 스택이 비어있을 때 고려
            # 스택이 비어있지 않음을 if문으로 따로 체크해줘도 괜찮지만
            # or 연산 또는 and 연산으로 다른 elif 조건문과 통합시킬 수 있다! by 재만님, 진용님
            
            if not stack:
                stack.append(string[char_idx])
                char_idx += 1
            elif stack[-1] == string[char_idx]:
                stack.pop()
                char_idx += 1
            else:
                stack.append(string[char_idx])
                char_idx += 1
    result.append(len(stack))

for tc in range(1, tests+1):
    print('#{} {}'.format(tc, result[tc]))
