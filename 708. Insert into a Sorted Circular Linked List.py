"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        #case 1: when the circular list is empty
        if not head:
            head=ListNode(insertVal)
            head.next=head
            return head
        min_val=float('inf')
        max_val=-float('inf')
        node=head
        while True:
            min_val=min(min_val,node.val)
            max_val=max(max_val,node.val)
            node=node.next
            if node==head:
                break
        #case two: if all elements in list are same
        if max_val==min_val:
            Next=head.next
            head.next=ListNode(insertVal)
            head.next.next=Next
        #case three: if the insertVal is above the max val
        elif insertVal>=max_val:
            node=head
            while True:
                if node.val==max_val and node.next.val!=max_val:
                    Next=node.next
                    node.next=ListNode(insertVal)
                    node.next.next=Next
                    break
                node=node.next
        #case four: if the insertVal is below the min val
        elif insertVal<=min_val:
            node=head
            father=None
            while True:
                if father and father.val!=min_val and node.val==min_val:
                    father.next=ListNode(insertVal)
                    father.next.next=node
                    break
                father=node
                node=node.next
        #case five: if the insertVal is within min val and max val
        elif min_val<insertVal<max_val:
            node=head
            while True:
                if node.val<=insertVal and node.next.val>=insertVal:
                    Next=node.next
                    node.next=ListNode(insertVal)
                    node.next.next=Next
                    break
                node=node.next
        return head
