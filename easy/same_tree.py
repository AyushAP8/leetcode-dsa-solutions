import time

'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
      
class soln1:
    '''Runtime: 47 ms, faster than 50.39% of Python3 online submissions for Same Tree.
    Memory Usage: 14 MB, less than 29.45% of Python3 online submissions for Same Tree.
    '''
    def is_same_tree(self, tree1: treeNode, tree2: treeNode) -> bool:
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.value == tree2.value:
            return self.is_same_tree(tree1.left, tree2.left) and self.is_same_tree(tree1.right, tree2.right)
        else:
            return False
        
class soln2:
    def is_same_tree(self, tree1: treeNode, tree2: treeNode) -> bool:
        if not tree1 or not tree2:
            return True
        elif tree1 and tree2 and tree1.value == tree2.value:
            return self.is_same_tree(tree1.left, tree2.left) and self.is_same_tree(tree1.right, tree2.right)
        else:
            return False

test = soln1()


tree1 = treeNode(1); tree1.left = treeNode(2);
tree2 = treeNode(1); tree2.left = treeNode(None); tree2.right = treeNode(2)
start_time = time.perf_counter()
ans = test.is_same_tree(tree1, tree2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

tree1 = treeNode(1); tree1.left = treeNode(2); tree1.right = treeNode(3)
tree2 = treeNode(1); tree2.left = treeNode(2); tree2.right = treeNode(3)
start_time = time.perf_counter()
ans = test.is_same_tree(tree1, tree2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

tree1 = treeNode(1); tree1.left = treeNode(2); tree1.right = treeNode(1)
tree2 = treeNode(1); tree2.left = treeNode(1); tree2.right = treeNode(2)
start_time = time.perf_counter()
ans = test.is_same_tree(tree1, tree2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")