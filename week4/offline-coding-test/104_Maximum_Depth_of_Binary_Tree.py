# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
이진 트리 데이터 
최대 깊이 반환

root - 가장 먼 leaf 까지의 노드 수 

이진 트리 - 순회 - 큐
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        # 왼쪽 서브 트리 깊이
        left_visited = self.maxDepth(root.left)

        # 오른쪽 서브 트리 깊이
        right_visited = self.maxDepth(root.right)

        # 왼쪽 서브 트리와 오른쪽 서브 트리 중 깊이가 더 깊은 서브 트리의 깊이 값 + 1(루트 자신)
        result = max(left_visited, right_visited) + 1
        
        return result