# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

def queue(n):
    # 시간 초과 방지를 위해 queue 라이브러리 사용
    import queue
    # 선언 및 초기화
    cards = queue.Queue()

    #cards = []

    # 1 ~ N 카드 쌓기
    for i in range(1, n + 1):
        #cards.append(i)
        cards.put(i)
    
    #while len(cards) > 1:
    while cards.qsize() > 1:
        # pop(0): 맨 앞 원소를 pop 하고, 그 뒤 원소들을 앞으로 당겨주는 연산으로 시간복잡도가 O(N) -> while문 돌아서 O(N^2)이 됨 => 시간초과 
        #cards.pop(0)
        #move = cards.pop(0)
        #cards.append(move)

        cards.get()
        move = cards.get()
        cards.put(move)
    
    return cards.queue[0]
        
if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())
    # n = int(input())

    result = queue(n)

    # print(int(queue(n)))
    print(result)