
def find_set(x):
    while x != group[x]:
        x = group[x]

    return x


def union(n1, n2):
    root1 = find_set(n1)
    root2 = find_set(n2)

    group[root2] = root1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N: 마을 사람 수 / M: 관계 수

    group = [num for num in range(N+1)]

    for _ in range(M):
        person1, person2 = map(int, input().split())

        union(person1, person2)

    # 그룹 수 count
    cnt = [0] * (N+1)
    for person in range(1, N+1):
        group_rep = find_set(person) # person이 속한 그룹의 대표자 
        cnt[group_rep] = 1

    result = sum(cnt)
    print('#{} {}'.format(tc, result))
