import time

'''Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class soln1:
    '''Runtime: 40 ms, faster than 74.11% of Python3 online submissions for Invert Binary Tree.
    Memory Usage: 13.9 MB, less than 57.29% of Python3 online submissions for Invert Binary Tree.'''
    def invert_tree(self, root: treeNode) -> treeNode:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
        
        
tree1 = treeNode(1); tree1.left = treeNode(2);
tree2 = treeNode(1); tree2.left = treeNode(None); tree2.right = treeNode(2)
start_time = time.perf_counter()
test = soln1()
ans = test.invert_tree(tree1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

tree1 = treeNode(1); tree1.left = treeNode(2); tree1.right = treeNode(3)
tree2 = treeNode(1); tree2.left = treeNode(2); tree2.right = treeNode(3)
start_time = time.perf_counter()
test = soln1()
ans = test.invert_tree(tree1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

tree1 = treeNode(1); tree1.left = treeNode(2); tree1.right = treeNode(1)
tree2 = treeNode(1); tree2.left = treeNode(1); tree2.right = treeNode(2)
start_time = time.perf_counter()
test = soln1()
ans = test.invert_tree(tree1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")