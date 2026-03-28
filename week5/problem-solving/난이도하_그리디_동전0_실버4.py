# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
def greedy(coins, k):
    memo = {}
    count = 0
    result = 0
    
    coins.sort(reverse=True)
    
    for coin in coins:
        count = k // coin

        if count > 0:
            result += count
            
            k = k % coin
            
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())

    coins = []

    for i in range(n):
        coin = int(input())
        
        coins.append(coin)

    print(greedy(coins, k))