# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.
#Floyd's Hare and Tortoise Algo
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast.next:
                if fast.next.next:
                    fast = fast.next.next
                    slow = slow.next
                else: return False
                if slow == fast: return True
        return False

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = ListNode(5)
print(hasCycle(head))

        