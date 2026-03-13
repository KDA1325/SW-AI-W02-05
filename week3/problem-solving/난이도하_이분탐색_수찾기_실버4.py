# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

def binary_search(arr, arr_target):
    result = []

    arr.sort()

    for i in range(len(arr_target)):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == arr_target[i]:
                result.append(1)
                break # 값을 찾으면 반드시 while 종료 
            
            elif arr[mid] > arr_target[i]:
                right = mid - 1

            elif arr[mid] < arr_target[i]:
                left = mid + 1

        if left > right:
            result.append(0)

    return result

if __name__ == '__main__':
    n = input()
    n = int(n)

    arr = list(map(int, input().split()))
    
    m = input()
    m = int(m)

    arr_target = list(map(int, input().split()))

    result = binary_search(arr, arr_target)

    # print(result)

    for i in range(len(result)):
        print(result[i])