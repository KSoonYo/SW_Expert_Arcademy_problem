

operators = {
        '-':1,
        '+':2,
        '*':3,
        '/':4,
    }



def calculator(operator, num1, num2):
    result = 0
    if operators[operator] == 1:
        result = num1 - num2
    elif operators[operator] == 2:
        result = num1 + num2
    elif operators[operator] == 3:
        result = num1 * num2
    else:
        result = num1 / num2
    
    return int(result)

def post_order(n):
    if left[n] and right[n]:
        num1_idx = post_order(left[n])
        num2_idx = post_order(right[n])
        num1 = tree[num1_idx]
        num2 = tree[num2_idx]
        now = tree[n]
        tree[n] = calculator(now, num1, num2)

    return n

for tc in range(1, 11):
    
    v = int(input())
    tree = [0] * (v+1)
    left = [0] * (v+1)
    right = [0] * (v+1)

    for v_idx in range(1, v+1):
        input_data = input().split()
        

        if len(input_data) > 3:
            tree[v_idx] = input_data[1]
            left[v_idx] = int(input_data[2])
            right[v_idx] = int(input_data[3])
        else:
            tree[v_idx] = int(input_data[1])
    
    # 후위 순회로 각 방향의 마지막 leaf 노드부터 연산을 거치기 
    post_order(1)
    result = tree[1]
    print('#{} {}'.format(tc, result))