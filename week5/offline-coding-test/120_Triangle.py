"""
삼각형 배열이 주어졌을 때, 위쪽에서 아래쪽으로 이동하는 경로의 최소 합을 반환하십시오.
각 단계에서, 현재 행의 인덱스 i에 있을 때 아래 행의 인덱스 i 또는 i + 1로 이동할 수 있습니다.

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle 요소 하나씩 돌면서 제일 작은 값 찾아서 저장하고 그 값 더하기?
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        selected = []
        tmp = 0
        result = 0

        for i in range(len(triangle)):
            # triangle 맨 첫 요소는 어차피 수 하나니까 바로 넣기 
            if i == 0:
                selected.append(triangle[i][0])
            else:
                # 두번째 요소부터 내부 요소 for문으로 접근
                for j in range(len(triangle[i])):
                    if j <= len(triangle[i]) - 2:
                        tmp = triangle[i][j]
                        #print(tmp)
                        if tmp > triangle[i][j + 1]:
                            tmp = triangle[i][j + 1]
                        else:
                          break
                
                selected.append(tmp)

        #print(selected)
        
        result = sum(selected)

        return result

