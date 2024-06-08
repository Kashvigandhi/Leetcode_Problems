class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode(0) #creating dummy node and traversing node
        while list1 and list2:#if list1 val is smaller than or equal to list2 value, cur is linked to list1, else to list2
            if(list1.val <= list2.val): 
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
    
        cur.next = list1 if list1 else list2 #attach remaining nodes of either list
       
        return dummy.next #returning dummy.next, which is the head
    
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(4)
p1.next = p2
p2.next = p3
q1 = ListNode(1)
q2 = ListNode(3)
q3 = ListNode(4)
q4 = ListNode(5)
q1.next = q2
q2.next = q3
q3.next = q4
s = Solution()
res = s.mergeTwoLists(p1,q1)
while(res):
    print(res.val)
    res = res.next

