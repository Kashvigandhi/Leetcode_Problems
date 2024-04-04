class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p1 = head
    while(p1.next != None):
        p2 = p1.next
        while((p1.val == p2.val) and p2 != None):
            p1.next = p2.next
            p2 = p2.next
        p1 = p1.next
    p3 = head
    while(p3.next != None):
        print(p3.val)
        p3 = p3.next
    
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

deleteDuplicates(l1)