# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#In-order traversal: left-root-right
# use a stack to store nodes.
# when the peak element has left child, add the left child. When there is no left child, pop the element and add the value into res.
# For the popped element, we need to know if it has right child. If yes, add the right element into the stack.
# Doing such iteratively until the stack is empty.
# For each element, we need a boolean value to mark is its left child has been visited or not. Otherwise the stack will fall into dead loop.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack=[[root,False]]
        res=[]
        while stack:
            if stack[-1][0].left!=None and stack[-1][1]==False:
                stack[-1][1]=True
                stack.append([stack[-1][0].left,False])
            else:
                stack[-1][1]=True
            if stack[-1][1]==True:
                node,visit=stack.pop()
                res.append(node.val)
                if node.right!=None:
                    stack.append([node.right,False])
        return res
