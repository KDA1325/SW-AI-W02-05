# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630


def color_check(x, y, size):
    # 각 구역의 첫번째 칸 색을 저장
    ## 첫 칸의 색을 기준으로 for문을 돌며 다른 색이 하나라도 있다면 False 반환     
    first = paper[x][y]

    # 현재 구간이 모두 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if not paper[i][j] == first:
                return False
    
    return True

def divide_conquer(x, y, size):
    white = []
    blue = []
    
    ## 구간이 모두 같은 색일 때
    if color_check(x, y, size):
        # 첫번째 칸이 0 == white == 1,0 반환
        if paper[x][y] == 0:
            return [1, 0]
        
        # 첫번째 칸이 1 == blue == 0,1 반환
        else:
            return [0, 1]

    # 사분면을 모두 반으로 나누기    
    half = size // 2

    r1 = divide_conquer(x, y, half)
    r2 = divide_conquer(x, y + half, half)
    r3 = divide_conquer(x + half, y, half)
    r4 = divide_conquer(x + half, y + half, half)

    # result에서 [0] 위치에 저장된 값이 white 여부
    ## white면 모든 result [0] 위치에 1이 저장되어있기 때문에 저장된 값의 합이 총 white 구역 수와 같음
    white = r1[0] + r2[0] + r3[0] + r4[0]
    
    # result에서 [1] 위치에 저장된 값이 blue 여부
    ## blue면 모든 result [1] 위치에 1이 저장되어있기 때문에 저장된 값의 합이 총 white 구역 수와 같음
    blue = r1[1] + r2[1] + r3[1] + r4[1]

    return [white, blue]

if __name__ == '__main__':
    n = int(input())

    paper = []
    
    for i in range(n):
        row = list(map(int, input().split()))
        paper.append(row)

    result = divide_conquer(0, 0, n)

    print(result[0])
    print(result[1])