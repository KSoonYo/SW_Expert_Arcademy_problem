
tests = 10
for tc in range(1, tests+1):
    N = int(input())
    expression = input()
    # 연산자 스택
    operator_stack = []

    # 출력 스택
    print_stack = []

    operator_priority = {
        '+': 1,
        '*': 2
    }
    # 중위 표기식 -> 후위 표기식
    top = -1
    for elem in expression:
        if elem.isdigit():
            print_stack.append(elem)
        else:
            if not operator_stack:
                operator_stack.append(elem)
            else:
                # 스택 안의 우선순위보다 들어오는 연산자의 우선순위가 높으면
                # => operator_stack 에 push()
                if operator_priority[elem] > operator_priority[operator_stack[top]]:
                    operator_stack.append(elem)
                else: # 그밖의 경우면
                    # 들어오는 연산자보다 작은 우선순위의 스택 안 연산자를 만날 때까지
                    # pop() -> 출력부에 저장
                    while True:
                        if not operator_stack:
                            operator_stack.append(elem)
                            break
                        elif operator_priority[operator_stack[top]] < operator_priority[elem]:
                            operator_stack.append(elem)
                            break
                        else:
                            print_stack.append(operator_stack.pop())
    # 수식이 끝나고 스택이 비어있지 않은 경우
    # 남은 연산자를 pop()하여 출력부에 저장
    while operator_stack:
        print_stack.append(operator_stack.pop())

    # 계산하기
    # 피연산자는 stack에 push
    # 연산자를 만나면
    # stack에서 피연산자 두개를 뽑은 뒤
    # 연산하고 stack에 다시 push()

    calculator = []

    for print_elem in print_stack:
        if print_elem.isdigit():
            calculator.append(int(print_elem))
        else:
            # 피연산자 두 개를 pop()
            num1 = calculator.pop()
            num2 = calculator.pop()
            # '+'이면 두 값을 더한 결과값을 계산기에 push
            # '*'이면 두 값을 곱한 결과값을 계산기에 push
            if operator_priority[print_elem] == 1:
                calculator.append(num2 + num1)
            else:
                calculator.append(num2 * num1)

    # 최종 결과값 반환
    print('#{} {}'.format(tc, calculator.pop()))

