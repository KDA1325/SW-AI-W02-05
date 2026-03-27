# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
"""
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램 작성

input: n
output: n번째 피보나치 수 출력

ex) 10
-> 
55
"""

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]

if __name__ == '__main__':
    n = int(input())

    print(fibonacci(n))