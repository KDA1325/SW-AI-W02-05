# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
"""
첫 줄의 컴퓨터 수는 vertices
직접 연결된 컴퓨터 쌍의 수는 edges
감염된 컴퓨터 수는 첫 감염 컴퓨터로 인해 연결되어 감염된 컴퓨터의 수 = 전체 감염 컴퓨터 수 - 1 = 끊기지 않고 연결된 노드의 수 - 1

이 문제는 인접한 노드들을 순회해야 하니까 BFS로 풀기 -> 큐 사용
start는 1 고정 
"""
from collections import deque

def bfs(vertices, edges):
    # start가 1로 고정이기 때문에 Key Error를 피하기 위해 범위를 1~vertices로 해야 함
    graph = { vertex: [] for vertex in range(1, vertices + 1) }
    visited = []
    
    start = 1
    
    # 큐를 만들 땐 반드시 그냥 start가 아니라 [start]로 노드 자체를 넣기 
    queue = deque([start])
    visited.append(start)

    # 컴퓨터의 연결은 무방향 연결이기 때문에 순서가 바뀐 edge도 추가해야 함
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    while queue:
        deque_item = queue.popleft()

        for neighbor in graph[deque_item]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    result = len(visited) - 1

    return result

if __name__ == '__main__':
    vertices = int(input())

    total_edges = int(input())

    edges = []

    for i in range(total_edges):
        a, b = map(int, input().split())

        edges.append([a, b])

    print(bfs(vertices, edges))



