# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        result = head

        sum = 0
        isOver10 = 0

        # l1, l2의 끝까지 순회(l1, l2 중 하나만 끝에 도달해도 탈출)
        while l1 is not None and l2 is not None:
            # 각 자릿수의 l1, l2 값을 더함
            ## 자릿수의 합이 10 이상이면 다음 자릿수에 1을 더하기 위한 isOver10 변수
            sum = l1.val + l2.val + isOver10
        
            # 다음 연산을 위해 변수 초기화
            isOver10 = 0

            # 자릿수의 합이 10 이상이면 다음 자릿수에 1을 더하고 해당 자리엔 10으로 나눈 나머지만 저장
            ## new_node 라는 이름으로 새로운 노드를 생성 후 값을 넣어준다
            new_node = ListNode(sum % 10)
        
            # 자릿수의 합이 10 이상이면 다음 자릿수에 1을 더하기 위해 isOver10 변수를 1로 설정
            if sum >= 10:
                isOver10 = 1

            # result 노드의 다음 노드를 new_node로 설정
            result.next = new_node

            # result 노드를 result.next 노드로 설정(= new_node로 설정), 앞으로 나아감
            result = result.next

            # reslut 노드 뿐만 아니라 l1, l2 노드들도 앞으로 나아가며 각 자릿수 합을 구함
            l1 = l1.next
            l2 = l2.next

        # 첫 while문에서 탈출한 뒤 l1 노드가 더 남아있다면 추가 처리
        while l1 is not None:
            sum = l1.val + isOver10
        
            isOver10 = 0
            
            if sum >= 10:
                isOver10 = 1

            new_node = ListNode(sum%10)

            result.next = new_node
            result = result.next

            l1 = l1.next

        # 첫 while문에서 탈출한 뒤 l2 노드가 더 남아있다면 추가 처리
        while l2 is not None:
            sum = l2.val + isOver10
        
            isOver10 = 0
            
            if sum >= 10:
                isOver10 = 1

            new_node = ListNode(sum%10)

            result.next = new_node
            result = result.next
            
            l2 = l2.next

        # 마지막 자릿수의 합이 10 이상이라면 노드 하나 더 생성해서 1 넣어줌 
        if isOver10 == 1:
            new_node = ListNode(1)
            result.next = new_node

        return head.next 