# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, then they are the same
        if not p and not q:
            return True
        # If one of the nodes is None, or the values of the nodes are not equal, then the trees are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively compare the left children and the right children of the two nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)