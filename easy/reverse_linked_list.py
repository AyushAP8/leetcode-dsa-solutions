import time

from pyparsing import Optional
'''Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
 
class linkedListNode:
    def __init__(self, val=0, next=None):
       self.value = val
       self.next = next
    
    def __repr__(self):
        #if self.next == None:
        #    print("empty linked list")
        #else:
        #    print(self.value)
        #    self = self.next
        #    self.show()
            
        node = self.value
        print(node)
                
            
            
 
class soln1:
    def rev_list(self, head: linkedListNode) -> linkedListNode:
        '''Runtime: 68 ms, faster than 23.23% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.4 MB, less than 93.96% of Python3 online submissions for Reverse Linked List.'''
        prev, curr = None, head        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    

class soln2:
     def rev_list(self, head: linkedListNode) -> linkedListNode:
        prev, curr = None, head
        while curr != None:
           temp = curr.next 
           curr.next = prev
           curr = temp
           temp = curr
        return temp
            


test = soln2()


llist1 = linkedListNode(1); llist1.next = linkedListNode(2); llist1.next = linkedListNode(3)
llist1.next = linkedListNode(4); llist1.next = linkedListNode(5)
print(llist1)
print("---")
start_time = time.perf_counter()
ans = test.rev_list(llist1)
print(f"Ans = {llist1}, Time taken = {time.perf_counter() - start_time}")    