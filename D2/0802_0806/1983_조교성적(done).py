
TEST = int(input())


# 점수 리스트
grade = [
    'A+', 'A0', 'A-', 
    'B+', 'B0', 'B-', 
    'C+', 'C0', 'C-', 
    'D0'
]


for test_case in range(1, TEST+1):
    # 학생 수, K번째 학생
    # 주의: 총점을 정렬하고 K번째가 아닌 입력받은 순 대로 K번째 
    students, target = map(int, input().split())
    
    score_list = []

    # 학생들의 점수 입력받기
    for _ in range(students):
        score_list += [list(map(int, input().split()))]

    # 최종 점수 계산하기
    # 리스트에는 순서가 있으므로 순서대로 점수 계산하여 추가
    final_scores = []

    for score in score_list:
        final_score = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
        final_scores.append(final_score)

    # k번째 학생의 총점
    target_score = final_scores[target-1]

    # 점수 내림차순으로 정렬
    sorted_scores = sorted(final_scores, reverse = True)

    # 각 등급별 점수대 기록 사전
    scores_dict = {}

    # 각 등급의 비율
    rate = students // 10

    # 등급 구분선
    start_point = 0

    # 각 등급에 해당하는 점수들을 구분하여 기록
    for final_grade in grade:
        if not scores_dict.get(final_grade):
            scores_dict[final_grade] = sorted_scores[start_point:rate]
            start_point = rate
            rate += students // 10
        
        if rate > students:
            break
        
    # target 찾고 타겟의 등급 출력하기
    # target의 총점은 중복되지 않는다는 전제가 문제에 명시
    for key in scores_dict.keys():
        if target_score in scores_dict[key]:
            print(f'#{test_case} {key}')
