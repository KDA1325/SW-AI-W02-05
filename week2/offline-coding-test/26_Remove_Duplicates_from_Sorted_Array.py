class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 오름차순으로 정렬된 정수 배열 nums
        # 고유 요소가 한 번씩만 나타나도록 중복된 요소를 제자리에서 제거
        # 요소들의 상대적인 순서는 그대로 유지
         # k는 nums의 고유한 요소 개수라고 고려함
        # 중복된 값을 삭제한 후엔 고유 요소 k를 반환함
        # nums의 첫번째 k 요소들은 고유한 수를 정렬된 순서로 포함
        # k-1 인덱스 이후 요소들은 무시해도 됨
        a = 0
        k = 0
        
        # nums 처음부터 끝까지 for문으로 돌기
        for(int i = 0; i < nums.len()-1; i++):
            # 오름차순 정렬이기 때문에 인덱스 i의 요소가 인덱스 i + 1 요소(다음 요소)와 값이 같은지 비교 
            a = nums[i]
        
            if(a == nums[i + 1]):
                # 인덱스 i + 1의 요소가 인덱스 i 의 요소와 값이 같다면 pop으로 요소를 제거함
                # 인덱스 i + 1의 요소를 제거해야 for문을 돌면서 다음 요소에 제대로 접근할 수 있음 
                nums.pop[i + 1]

        # 중복된 요소가 다 제거된 후 남은 요소들의 개수(nums의 길이)를 고유한 요소 개수 k로 저장
        k = nums.len()

        # removeDuplicates는 int k를 반환
        return k
