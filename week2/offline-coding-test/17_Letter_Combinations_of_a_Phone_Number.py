"""
17. Letter Combinations of a Phone Number

2부터 9까지의 주어진 숫자로 이루어진 문자열에서 해당 숫자가 나타낼 수 있는 모든 문자 조합을 반환하기
순서는 상관없음

---
<숫자와 문자의 대응표>
숫자 1은 어떤 문자에도 대응되지 않음
2: a, b, c
3: d, e, f
4: g, h, i
5: j, k, l
6: m, n, o
7: p, q, r, s
8: t, u, v
9: w, x, y, z
---

제약 조건
1 <= digits.length < = 4
digits[i]는 ['2', '9']범위 내의 숫자
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_letters = {'2': 'abc', '3': 'def', '4': 'ghi', 
        '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []

        # index: digits 문자열 중 현재 단계에서 보고 있는 index 번호 
        # current_letters: 현재 단계까지 조합된 문자열 
        def backtrack(index, current_letters):
            if index == len(digits):
                # [["a", "d"], ["a", "e"], ...] 로 저장됨 
                # result.append(list(current_letters))
                
                # current_letters 리스트에 담긴 개별 문자들을 "문자열" 형식으로 합쳐서 result에 append()
                result.append("".join(current_letters))
                return

            # digits[index]에 위치한 숫자(문자)에 대응하는 알파벳(문자열)에 접근  
            # digits[index]에 대응되는 문자열의 문자 하나씩 시도
            for j in range(len(dict_letters[digits[index]])):
                # 1. 선택
                current_letters.append(dict_letters[digits[index]][j])
            
                # 2. 재귀
                backtrack(index + 1, current_letters)

                # 3. 취소: digits[index]에 대응되는 다음 조합을 만들기 위해 들어있는 문자를 뺌
                current_letters.pop()
        
        backtrack(0, [])

        return result