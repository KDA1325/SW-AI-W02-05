"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)

    # ---
    # arr = [0] * n
    # rotated = [arr] * n

    # 이 방식으로 rotated 배열을 생성하면 모든 행이 마지막 행으로 채워지게 됨
    # -> 얕은 복사로 인해 [0][0] 요소만 바뀌어도 [1][0]과 [2][0]이 모두 바뀌게 됨
    # -> C언어에서 포인터만 지정한 것과 비슷한 경우가 됨

    # 얕은 복사로 복사된 배열은 서로 다른 객체를 가리키고 있지만 두 배열 안에 존재하는 요소는 같은 요소의 특징을 가지고 있게 됨
    # 한 배열의 요소가 뮤터블 객체라면 복사된 배열의 요소도 뮤터블 객체의 특성을 띄게 됨
    # -> 한 배열에 뮤터블 객체인 리스트를 요소로 넣고 얕은 복사를 하면 복사된 배열에서 한 리스트 내부 요소를 수정할 때 나머지 리스트 내부 요소까지 함께 변경됨
    # ---

    # 리스트 컴프리헨션으로 각 행마다 독립된 메모리 공간을 갖도록 새로운 리스트를 만들어 줌
    rotated = [[0] * n for i in range(n)]

    # 2차원 배열 접근은 rotated[row(i)][col(j)]

    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동 
    for i in range(n):
        for j in range(n):
            # rotated[j][i] = matrix[n-1-i][j]
            rotated[j][n-1-i] = matrix[i][j]
    
    return rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)