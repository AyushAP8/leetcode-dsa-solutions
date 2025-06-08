import time
'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''
class linkedListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class soln1:
    def merge_two_list(self, list1: linkedListNode, list2: linkedListNode) -> linkedListNode:
        head = linkedListNode()
        tail = head

        while True:
            
            if list1 and list2 and list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                print("<=", tail.next.val)
                continue
            elif list1 and list2 and list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
                print(">", tail.next.val)
                continue
            tail = tail.next
            
            if list1:
                tail.next = list2
                break
            if list2:
                tail.next = list1
                break

        return head
                
llist1 = linkedListNode(1); llist1.next = linkedListNode(2); llist1.next.next = linkedListNode(4)
llist2 = linkedListNode(1); llist2.next = linkedListNode(3); llist2.next.next = linkedListNode(4)
start_time = time.perf_counter()
test = soln1()
ans = test.merge_two_list(llist1, llist2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")
while ans is not None:
    print(ans.val)
    ans = ans.next
            
        