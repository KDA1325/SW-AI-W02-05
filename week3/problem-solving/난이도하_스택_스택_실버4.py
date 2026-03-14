# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
"""
 문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
"""
def push(stk, x):
    stk.append(x)

def pop(stk):
    print("pop")
    if len(stk) == 0:
        print(-1)
    
    else:
        x = stk.pop()
        print(x)

def size(stk):
    stk_size = len(stk)
    print(stk_size) 

def empty(stk):
    if len(stk) == 0:
        print(1)
    else:
        print(0)

def top(stk):
    if len(stk) == 0:
        print(-1)
    else:
        print(stk[len(stk) - 1])

if __name__ == '__main__':  
    n = input()
    n = int(n)

    inputs = []
    stk = []

    # for cmd in cmd_arr 처럼 리스트 요소 자체를 돌게해보기 
    for i in range(n):
        cmd = list(map(str, input().split()))
        inputs.append(cmd)
    # print(inputs)
    # [['pop'], ['top'], ['push', '123'], ['pop'], ['top'], ['pop'], ['top']]
    for j in range(len(inputs)):
        # print("output")
        if inputs[j][0] == "push":
            # push 문자열과 x 값은 이중으로 들어감
            x = int(inputs[j][1])
            push(stk, x)
        elif inputs[j] == "pop":
            pop(stk)
        elif inputs[j] == "size":
            size(stk)
        elif inputs[j] == "empty":
            empty(stk)
        elif inputs[j] == "top":
            top(stk)