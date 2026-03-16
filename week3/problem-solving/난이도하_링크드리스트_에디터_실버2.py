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

    result = ''.join(left_s + right_s[::-1])

    return result

if __name__ == '__main__':
    import sys
    
    strings = str(sys.stdin.readline().strip('\n'))
    result = LinkedList(strings)
    print(result)