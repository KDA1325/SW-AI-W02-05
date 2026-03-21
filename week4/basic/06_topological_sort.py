"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    ## queue 미리 만들기 
    queue = deque()
    
    # vertex의 수를 길이로 하는 graph 딕셔너리 만들기
    ## graph = { 0:[], 1:[], ... } 만들어짐
    graph = { vertex:[] for vertex in range(vertices) }

    # 진입 차수 계산을 위해 vertex 수만큼 초기 value가 모두 0인 리스트 만들기
    indegrees =[0] * vertices 

    # TODO: 그래프 구성 및 진입 차수 계산
    # edges의 edge 케이스 하나씩 순회하면서 graph 딕셔너리 채우기
    for e in edges:
        # graph = {0:[1, 2], 1:[3], 2:[], 3:[]}
        graph[e[0]].append(e[1])

        #(0, 1) = 0 -> 1 = 0이 1을 가리키고 있다 = 1의 진입 차수 1 증가
        indegrees[e[1]] += 1

    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for i in range(vertices):
        if indegrees[i] == 0:
            queue.append(i)
    
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        deque_item = queue.popleft()

        # result = pop된 순서 = deque_item을 result에 추가
        result.append(deque_item)

        # graph를 통해 deque_item의 인접 정점들 순회
        for neighbor in graph[deque_item]:
            # 진입 차수 감소
            indegrees[neighbor] -= 1

            # 진입 차수가 0이 되었다면 바로 큐에 넣음
            if indegrees[neighbor] == 0:
                queue.append(neighbor)    
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
