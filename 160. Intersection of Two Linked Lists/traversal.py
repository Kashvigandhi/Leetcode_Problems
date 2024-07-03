# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    countA = 0
    countB = 0
    tempA = headA
    tempB = headB
    while tempA or tempB:
        if tempA:
            countA += 1
            tempA = tempA.next
        if tempB:
            countB += 1
            tempB = tempB.next
    tempA = headA
    tempB = headB
    if countA > countB:
        for i in range(countA - countB):
            tempA = tempA.next
    if countB > countA:
        for i in range(countB - countA):
            tempB = tempB.next
    while tempA:
        if tempA == tempB : return True
        tempA = tempA.next
        tempB = tempB.next
    return False

 
root1 = ListNode("a1")
root2 = ListNode("b1")
root1.next = ListNode("a2")
root2.next = ListNode("b2")
root1.next.next = ListNode("c1")
root2.next.next = ListNode("b3")
root2.next.next.next = root1.next.next
root1.next.next.next = ListNode("c2") 
root1.next.next.next.next = ListNode("c3") 
print(getIntersectionNode(root1,root2))
