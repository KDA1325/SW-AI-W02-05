# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
"""
        #for j in range(indegrees)
        # 각 정점의 indegree 수만큼 반복문 돌려서 neighbors[i[j]]로 접근? 해서 
        # edge = (neighbor, vertex)
        # edges.append(edge)
        
        # 일반적인 위상정렬 방식대로 큐 사용
        # 진입차수가 0인 노드를 먼저 큐에 저장, visited에 저장
        # pop하면서 다음 진입차수가 0인 노드들 저장
        ## 이 때 진입 차수가 0인 노드들을 한번에 저장하고 한번에 빼서 작업에 걸리는 시간을 둘 중 큰 시간만 적용되도록 한다
        ### ex) visited = [1, 2&4, 3&5&6, 7 ] = 작업에 걸린 시간 =[5초, 6(&1)초, 8(3&1)초, 4초] -> 총 23초 
"""
from collections import deque

def solution():
    vertices = int(input())

    times = [0] * (vertices + 1)
    indegrees = [0] * (vertices + 1)

    # Dynamic Programming: 이전 결과를 이용해 문제를 단계적으로 해결
    # 알고리즘에서 관습적으로 dp[i]를 i까지 계산한 결과, dp[i][j]를 i, j상태에서의 결과로 사용함
    ## dp[i] = i번 작업의 완료 시간
    dp = [0] * (vertices + 1)

    graph = { vertex: [] for vertex in range(vertices+1) }
    
    for vertex in range(1, vertices + 1):
        data = list(map(int, input().split()))
        time = data[0]
        indegree = data[1]
        neighbors = data[2:]

        times[vertex] = time
        indegrees[vertex] = indegree

        for neighbor in neighbors:
            graph[neighbor].append(vertex)
    
    queue = deque()

    for vertex in range(1, vertices + 1):
        if indegrees[vertex] == 0:
            queue.append(vertex)
            dp[vertex] = times[vertex]

    while queue:
        deque_item = queue.popleft()

        for neighbor in graph[deque_item]:
            # deque_item을 먼저 끝내고 neighbor를 수행하는 경우의 완료 시간 반영 
            # dp[deque_item] = 현재 작업이 끝나는 시간
            # dp[deque_item] + times[neighbor] = neighbor의 완료 시간
            dp[neighbor] = max(dp[neighbor], dp[deque_item] + times[neighbor])

            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    print(max(dp))

solution()