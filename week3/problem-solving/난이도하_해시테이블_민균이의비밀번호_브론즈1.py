# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

def find_word(words):
    for word in words:
        if word[::-1] in words:
            return word


if __name__ == '__main__':
    n = int(input())
    words = set()

    for i in range(n):
        word = str(input())
        words.add(word)

    result = find_word(words)

    result_len = len(result)

    mid = result_len // 2
    result_s = result[mid]

    print(result_len)
    print(result_s)