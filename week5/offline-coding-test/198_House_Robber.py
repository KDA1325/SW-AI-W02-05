"""
집에숨겨진돈=nums
인접한두집에 
침입하면경찰신고
경찰에게 
발각되지않고털수있는최대금액
-> 
퐁당퐁당금액저장하기
첫집은무조건터나??

재귀?
for?

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 일단 턴 집에있던 돈들을 dp에 담기 위해 dp 리스트 만들어주기
        dp = [0] * (len(nums))
        # print(dp)

        # 턴 집에있던 돈들의합
        total = 0

        # base case
        # 첫 집은 무조건 털어 
        dp[0] = nums[0]

        # 첫 집 털었으니까 다음은 무조건 다다음집
        for i in range(2, len(nums)):
            dp[i] = nums[i]

            i += 2

            if i >= len(nums):
                break


        print(dp)
        for j in range(len(dp)):
            print(dp[j])
            total += dp[j]

        #print(total)

        return total