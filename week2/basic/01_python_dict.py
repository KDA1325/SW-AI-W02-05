"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""

def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수
    
    Args:
        students: 학생 정보 딕셔너리 리스트
    
    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """

    # 평균 점수 이상인 학생 이름을 저장할 리스트 
    above_average_students = []

    # 모든 학생들의 점수를 저장할 리스트
    scores = []

    # TODO: 모든 학생의 점수를 리스트로 추출하세요    

    # 리스트 [딕셔너리]
    # students 리스트를 처음부터 끝까지 돌면서 key 값이 score인 value를 get
    # value 값을 scores 리스트에 요소로 저장 

    # 딕셔너리 get() 함수 사용
    # for i in range(len(students)):
    #     scores.append(students[i].get('score'))
        
    # 딕셔너리 직접 접근
    # for i in range(len(students)):
    #     scores.append(students[i]['score'])

    # 리스트 컴프리헨션 사용 
    # 컴프리헨션 구문에선 get() 함수 사용 불가
    scores = [students[i]['score'] for i in range(len(students))]

    # TODO: 평균 점수를 계산하세요
    average = sum(scores)/len(students)

    # TODO: 평균 이상인 학생들의 이름을 리스트로 추출하세요

    # 딕셔너리 get() 함수 사용
    # for i in range(len(scores)):
    #     if scores[i] >= average:
    #         above_average_students.append(students[i].get('name'))

    # 딕셔너리 직접 접근
    # for i in range(len(scores)):
    #     if scores[i] >= average:
    #         above_average_students.append(students[i]['name'])

    # 리스트 컴프리헨션 사용 
    # 컴프리헨션 구문에선 get() 함수 사용 불가
    above_average_students = [students[i]['name'] for i in range(len(scores)) if scores[i] >= average]

    # 반환값 두 개를 tuple로 묶어주기
    tuple = (average, above_average_students)

    return tuple

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")