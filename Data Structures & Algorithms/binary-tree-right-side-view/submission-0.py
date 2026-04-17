# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []

        def dfs_from_right(node, depth):
            if node == None:
                return None
            if depth == len(res):
                res.append(node.val)

            dfs_from_right(node.right, depth + 1)
            dfs_from_right(node.left, depth + 1)

        dfs_from_right(root, 0)

        return res