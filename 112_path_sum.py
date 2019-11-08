# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None: return False
        Q=deque([[root,root.val]])
        while Q:
            for _ in range(len(Q)):
                node,value=Q.popleft()
                if value==sum and node.left==None and node.right==None: return True
                if node.left!=None:
                    Q.append([node.left,value+node.left.val])
                if node.right!=None:
                    Q.append([node.right,value+node.right.val])
        return False

#note: Don't terminate the searching by the condition that (if sum value>target).
#Because the integer can be genative value. So the sum could be lower and lower.
