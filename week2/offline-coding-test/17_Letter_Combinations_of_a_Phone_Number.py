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
        # 출력값 리스트에 요소가 다 차면 종료
        # 한 조합: 숫자 개수가 문자 개수 -> 이걸 여러 개 담은 리스트를 반환

        # 각 숫자가 어떤 문자를 가지고 있는지 어케 알지 내가 넘겨줘야 하나??

        # 숫자 개수만큼 문자가 들어가는 조합
        output = ""

        # 조합들이 들어가는 리스트 
        result = []   

        # 백트래킹용 함수 하나 더 필요 
        def backtrack(start, current_combination):  
            nums = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
            ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
            ["t", "u", "v"], ["w", "x", "y", "z"]]
            # base case, 종료
            # 한 조합의 길이가 숫자 개수만큼 되면 -> 조합 하나가 완료된 것이라고 판단하고 종료하기 
            if len(current_combination) == len(digits):
                # result 리스트에 조합 넣어주기
                return result.append(list(current_combination))
            
            # start부터 len(digits)까지 숫자를 하나씩 시도
            for i in range(start, len(digits)):
                # 1. 선택
                # 현재 위치의 숫자 추가
                current_combination.append(nums[digits[i]][i])

                # 2. 탐색, 재귀
                # 중복되지 않게 i + 1로 다음 단계 이동
                # 만약 현재 i가 2라면, 다음 재귀에선 3이 되면서 겹치지 않는 다른 조합을 탐색할 수 있음
                backtrack(i + 1, current_combination)

                # 3. 취소
                # 다음 단계 진행을 위한 pop
                # 재귀에서 나와 i가 들어간 모든 경우의 수를 다 확인했으니 다음 단계 i를 넣기 위해 i를 pop
                current_combination.pop() 

        backtrack(1, [])
        return result