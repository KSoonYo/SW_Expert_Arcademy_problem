
tests = int(input())

for tc in range(1, tests+1):
    expression = input().split()
    calculator = []

    operators = {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4
    }

    #
    # flag = 1
    # for elem in expression:
    #     # 연산자라면
    #     if elem in operators:
    #         # 아직 연산자가 있음에도 stack의 남은 요소가 2개 미만인 경우
    #         if len(calculator) < 2:
    #             flag = 0
    #             break
    #         num1 = calculator.pop()
    #         num2 = calculator.pop()
    #         if operators[elem] == 1:
    #             calculator.append(num2 + num1)
    #         elif operators[elem] == 2:
    #             calculator.append(num2 - num1)
    #         elif operators[elem] == 3:
    #             calculator.append(num2 * num1)
    #         else:
    #             calculator.append(int(num2 / num1))
    #
    #     # 수식 종료
    #     elif elem == '.':
    #         break
    #
    #     else:
    #         calculator.append(int(elem))
    #
    # if not flag or not calculator or len(calculator) != 1:
    #     ans = 'error'
    # else:
    #     ans = calculator.pop()
    #
    # print('#{} {}'.format(tc, ans))
    #


    # ans = 0
    # for elem in expression:
    #     # elem이 연산자라면
    #     if elem in operators:
    #         # 아직 연산자가 있음에도 stack의 남은 요소가 2개 미만인 경우
    #         if len(calculator) < 2:
    #             ans = 'error'
    #             break
    #         num1 = calculator.pop()
    #         num2 = calculator.pop()
    #         if operators[elem] == 1:
    #             calculator.append(num2 + num1)
    #         elif operators[elem] == 2:
    #             calculator.append(num2 - num1)
    #         elif operators[elem] == 3:
    #             calculator.append(num2 * num1)
    #         else:
    #             calculator.append(num2 / num1)
    #
    #     # elem이 정수라면
    #     else:
    #         # 수식 종료
    #         if elem == '.':
    #             # 계산을 모두 마쳤으나 뽑을 결과값이 없다면
    #             if not calculator:
    #                 ans = 'error'
    #                 break
    #             else:
    #                 ans = calculator.pop()
    #                 # 계산을 모두 마치고 결과값을 뽑았는데도 계산기에 값이 더 남아있다면
    #                 # 형식이 잘못되어있는 것이므로 error
    #                 if calculator:
    #                     ans = 'error'
    #                     break
    #         else:
    #             calculator.append(int(elem))
    #
    # print('#{} {}'.format(tc, ans))

    try:
        for elem in expression:
            if elem.isdigit():
                calculator.append(int(elem))
            # 수식 종료 구문
            elif elem == '.':
                ans = calculator.pop()
                # 계산을 모두 마치고 결과값을 뽑았는데도 계산기에 값이 남아있다면
                # 형식이 잘못되어있는 것이므로 error
                if calculator:
                    ans = 'error'

            # 연산자인 경우
            else:
                num1 = calculator.pop()
                num2 = calculator.pop()
                if operators[elem] == 1:
                    calculator.append(num2 + num1)
                elif operators[elem] == 2:
                    calculator.append(num2 - num1)
                elif operators[elem] == 3:
                    calculator.append(num2 * num1)
                else:
                    calculator.append(num2 // num1)

    except IndexError:
        ans = 'error'
    # except KeyError:
    #     ans = 'error'

    print('#{} {}'.format(tc, ans))

