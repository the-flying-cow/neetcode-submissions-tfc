# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        tree1_nodes= []
        tree2_nodes= []

        def traverse1(node):
            if node==None:
                tree1_nodes.append(None)
                return

            tree1_nodes.append(node.val)
            traverse1(node.left)
            traverse1(node.right)
        
            
        traverse1(p)

        def traverse2(node):
            if node==None:
                tree2_nodes.append(None)
                return
            
            tree2_nodes.append(node.val)
            traverse2(node.left)
            traverse2(node.right)
            
        traverse2(q)

        if tree1_nodes == tree2_nodes:
            return True
        else:
            return False