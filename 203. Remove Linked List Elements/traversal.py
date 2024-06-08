# # Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def removeElement(head, val):
#     """
#     :type head: ListNode
#     :type val: int
#     :rtype: ListNode
#     """
#     previous = None
#     current = head
#     headToReturn = head
#     while(current != None):
#         if(current.val == val):
#             if(previous == None):
#                 previous = current
#                 current = current.next
#                 headToReturn = current
#                 del previous
#                 previous = None
#             else:
#                 current = current.next
#                 del previous.next
#                 previous.next = current
#         else:
#             previous = current
#             current = current.next
#     return headToReturn
# l1 = ListNode(7)
# l2 = ListNode(7)
# l3 = ListNode(7)
# l4 = ListNode(7)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# removeElement(l1,7)
a = [1]
b = a
del a
print(b)