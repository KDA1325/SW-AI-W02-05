# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
"""
비행기를 최대한 적게
한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도 됨(이미 방문한 국가여도)
-> visited 확인 안 해도 될 듯

국가의 수 N, 비행기의 종류 M
M개의 줄에 a b 쌍 입력(a와 b 왕복하는 비행기) -> 무방향 연결 그래프

테스트 케이스마다 한 줄 출력
상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수 출력 

답은 그냥 N - 1
"""

def solution():
    t = int(input())
    result = []

    for _ in range(t):
        n, m = map(int, input().split())

        for _ in range(m):
            a, b = map(int,input().split())

        result.append(n - 1)
    
    for i in range(t):
        print(result[i])

if __name__ == '__main__':
    solution()