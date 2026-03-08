"""
26. Remove Duplicates from Sorted Array

오름차순으로 정렬된 정수 배열 nums
고유 요소가 한 번씩만 나타나도록 중복된 요소를 제자리에서 제거
요소들의 상대적인 순서는 그대로 유지
k는 nums의 고유한 요소 개수라고 고려함
중복된 값을 삭제한 후엔 고유 요소 k를 반환함
nums의 첫번째 k 요소들은 고유한 수를 정렬된 순서로 포함
k-1 인덱스 이후 요소들은 무시해도 됨
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 요소 비교를 위해 임시로 저장할 변수 
        tmp = 0

        # 반환해야 하는 고유 요소 수 k
        k = 0   

        # 첫 for문을 돌면서 pop 해야 하는 nums의 요소 인덱스 번호를 저장할 리스트 
        idxs = []        

        # nums 처음부터 끝까지 for문으로 돌기
        for i in range(len(nums) - 1):

            # 오름차순 정렬이기 때문에 인덱스 i의 요소가 인덱스 i + 1 요소(다음 요소)와 값이 같은지 비교 
            tmp = nums[i]

            # 인덱스 i + 1의 요소가 인덱스 i 의 요소와 값이 같다면 둘 중 하나의 요소를 제거해야 함
            if(tmp == nums[i + 1]):
                # for문 안에서 pop을 진행하면 인덱스 오류 발생
                # 우선 pop 해야하는 요소의 인덱스 번호를 별도의 리스트에 저장
                idxs.append(i + 1)
                
        # 저장한 인덱스 번호를 통해 앞에서부터 순서대로 pop을 진행해도 똑같이 인덱스 오류 발생
        # 이를 방지하기 위해 인덱스 번호 리스트를 뒤집어 nums의 마지막 요소부터 pop을 진행 
        reversed_idxs = list(reversed(idxs))

        # 뒤집은 인덱스 번호를 통해 뒤부터 순서대로 pop 진행
        for i in range(len(reversed_idxs)):
            nums.pop(reversed_idxs[i])

        # 중복된 요소가 다 제거된 후 남은 요소들의 개수(nums의 길이)를 고유한 요소 개수 k로 저장
        k = len(nums)

        # removeDuplicates는 int k를 반환
        return k
