# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

def LinkedList(strings):
    left_s = []
    right_s =[]

    import sys
    
    for s in strings:
        left_s.append(s)

    m = int(input())
    
    while m > 0:
        cmd = sys.stdin.readline().split()

        if cmd[0] == "L":
            if left_s:
                left = left_s.pop()
                right_s.append(left)
        elif cmd[0] == "D": 
            if right_s:
                right = right_s.pop()
                left_s.append(right)
        elif cmd[0] == "B":
            if left_s:
                left_s.pop()
        elif cmd[0] == "P":
            s = cmd[1]
            left_s.append(s)

        m -= 1

    # 단순 문자열 형태로 출력하기 위해 join 사용
    ## right_s에 pop, append 작업을 반대로 했기 때문에 출력할 때 반대로 돌려서 출력해줘야 함
    result = ''.join(left_s + right_s[::-1])

    return result

if __name__ == '__main__':
    import sys
    # sys.stdin.readline()은 개행 문자 \n까지 입력 받음 -> .strip('\n')으로 개행 문자 없이 입력 받기 가능
    strings = str(sys.stdin.readline().strip('\n'))
    result = LinkedList(strings)
    print(result)