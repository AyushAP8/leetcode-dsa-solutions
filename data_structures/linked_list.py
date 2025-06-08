#from collections import Optional

class linkedListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val
        
class linkedList:
    def __init__(self, nodes: list = None):
        self.head = None
        for i, val in enumerate(nodes):
            if i == 0:
                node = linkedListNode(val)
                self.head = node
            else:
                node.next = linkedListNode(val)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(str(n) for n in nodes)
    
    def __iter__(self) -> linkedListNode:
        node = self.head
        while node:
            yield node
            node = node.next
    
    def add_head(self, node: linkedListNode):
        node.next = self.head
        self.head = node
    
    def add_tail(self, node: linkedListNode):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        node.next = None
        
        '''if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node'''
        
    
    def add_after(self, node: linkedListNode, target_node: int):
        current_node = self.head
        while current_node:
            print(current_node.val)
            if current_node.val == target_node:
                node.next = current_node.next
                current_node.next = node
                return
            current_node = current_node.next
        raise Exception("value not found in the linked list")
    
    def add_before(self, node: linkedListNode, target_node: int):
        current_node = self.head
        while current_node.next.val != target_node:
            current_node = current_node.next
        node.next = current_node.next
        current_node.next = node
        
    def remove_node(self, target_node: int):
        current_node = self.head
        while current_node.next.val != target_node:
            current_node = current_node.next
        current_node.next = current_node.next.next
    
    
    
#test
llist = linkedList([1,2,3,4])
print(llist)
llist.add_head(linkedListNode(5))
print(llist)
llist.add_tail(linkedListNode(6))
print(llist)
llist.add_after(linkedListNode(4), 4)
print(llist)
llist.add_before(linkedListNode(4), 4)
print(llist)
llist.add_before(linkedListNode(2), 2)
print(llist)
print("---")
llist.remove_node(2)
print(llist)
llist.remove_node(2)
print(llist)