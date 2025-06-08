import time


'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

class linkedListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class soln1:
    def has_cycle(self, head: linkedListNode) -> bool:
        hmap = {}
        pos = 0
        while head:
            if head.val in hmap:
                return True
            hmap[head.val] = pos
            pos += 1
            head = head.next
        return False
    
class soln2:
    '''Runtime: 101 ms, faster than 28.66% of Python3 online submissions for Linked List Cycle.
    Memory Usage: 17.5 MB, less than 66.92% of Python3 online submissions for Linked List Cycle.'''
    def has_cycle(self, head: linkedListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
    
llist1 = linkedListNode(1); llist1.next = linkedListNode(2); llist1.next.next = linkedListNode(4)
llist1.next.next.next = linkedListNode(5); llist1.next.next.next.next = linkedListNode(6)
llist1.next.next.next.next.next = llist1.next
llist2 = linkedListNode(1); llist2.next = linkedListNode(2); llist2.next.next = linkedListNode(4)

start_time = time.perf_counter()
test = soln2()
ans = test.has_cycle(llist1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")
'''while ans is not None:
    print(ans.val)
    ans = ans.next'''