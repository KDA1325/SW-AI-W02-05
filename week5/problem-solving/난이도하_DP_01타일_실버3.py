# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
"""
input: n
output: 길이가 n인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력
"""

def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1

    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746  

    return dp[n] % 15746   

if __name__ == '__main__':
    n = int(input())

    print(solution(n))