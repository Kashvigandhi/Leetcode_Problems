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
    visitedNodes = []
    tempA = headA
    tempB = headB
    while(tempA != None or tempB != None):
        if((tempA == tempB)  or (tempA in visitedNodes)):
            return tempA
        if ((tempB in visitedNodes)):
            return tempB
        visitedNodes.append(tempA)
        visitedNodes.append(tempB)
        tempA = tempA.next
        tempB = tempB.next
    if (tempA):
        while(tempA):
            if tempA in visitedNodes : return tempA
            tempA = tempA.next
    if (tempB):
        while(tempB):
            if tempB in visitedNodes : return tempB
            tempB = tempB.next
    return None
root1 = ListNode("a1")
root2 = ListNode("b1")
root1.next = ListNode("a2")
root2.next = ListNode("b2")
root1.next.next = ListNode("c1")
print(root1.next.next)
root2.next.next = ListNode("b3")
root2.next.next.next = root1.next.next
root1.next.next.next = ListNode("c2") 
root1.next.next.next.next = ListNode("c3") 
print(getIntersectionNode(root1,root2))
