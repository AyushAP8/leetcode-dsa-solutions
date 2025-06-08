import time

from idna import valid_contextj

'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''
class treeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class soln1:
    def diameter_binary_tree(self, root: treeNode) -> int:
        #if not list - UnboundLocalError: local variable 'diameter' referenced before assignment
        diameter = [0]
        
        def dfs(root: treeNode):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diameter[0] = max(diameter[0], 2 + left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return diameter[0]  
    
tree1 = treeNode(1); tree1.left = treeNode(2)
tree2 = treeNode(1); tree2.left = treeNode(5); tree2.right = treeNode(2); tree2.right.right = treeNode(6)
tree3 = treeNode(1); tree3.left = treeNode(5); tree3.right = treeNode(2); tree3.left.left = treeNode(5)
tree3.left.left.left = treeNode(5)

test = soln1()

start_time = time.perf_counter()
ans = test.diameter_binary_tree(tree1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.diameter_binary_tree(tree2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.diameter_binary_tree(tree3)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")