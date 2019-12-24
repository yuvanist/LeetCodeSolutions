'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c=0
        l3=head=ListNode(0)
        s=c
        while(l1 and l2):
            s=0
            s+=(l1.val+l2.val+c)
            l1=l1.next
            l2=l2.next
            l3.next=ListNode(s%10)
            l3=l3.next
            if s>9:
                c=1
            else:
                c=0
        while(l1):
            s=0
            s+=(l1.val+c)
            l1=l1.next
            l3.next=ListNode(s%10)
            l3=l3.next
            if s>9:
                c=1
            else:
                c=0
        while(l2):
            s=0
            s+=(l2.val+c)
            l2=l2.next
            l3.next=ListNode(s%10)
            l3=l3.next
            if s>9:
                c=1
            else:
                c=0
        if c:
            l3.next=ListNode(c)
        return head.next
            
            
            
#Time Complexity : O(max(m,n))
#Space Complexity: O(max(m,n))



