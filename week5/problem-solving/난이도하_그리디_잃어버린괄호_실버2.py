# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
"""
수식
가장 처음과 마지막 문자는 숫자
연속해서 두 개 이상의 연산자가 나타나지 않음
5자리보다 많이 연속되는 숫자는 없음
수는 0으로 시작할 수 있음
"""
def solution(ins):
    first = sum(map(int, ins[0].split('+')))

    for part in ins[1:]:
        first -= sum(map(int, part.split('+')))

    return first
    
if __name__ == '__main__':
    ins = input().split('-')

    print(solution(ins))