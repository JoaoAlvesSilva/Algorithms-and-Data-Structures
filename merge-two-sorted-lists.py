// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l = list1
        r = list2

        if l== None and r== None:
            return None
        elif l == None:
            head = r
            r = head.next
        elif r== None:
            head = l
            l = head.next
        elif l.val <= r.val:
            head = l
            l = head.next
        else:
            head = r
            r = head.next
        
        curr = head

        while (l!=None or r!=None):

            if l == None:
                temp = r
                r = temp.next

            elif r == None:
                temp = l
                l = temp.next

            elif l.val <= r.val:
                temp = l
                l = temp.next
            else:
                temp = r
                r = temp.next
        
            curr.next = temp
            curr = temp
        
        return head



        