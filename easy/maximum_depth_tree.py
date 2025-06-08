import time
from collections import deque

'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class soln1:
    '''Runtime: 44 ms, faster than 91.95% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 16.2 MB, less than 74.83% of Python3 online submissions for Maximum Depth of Binary Tree. 
    Ans = 2, Time taken = 3.7999999999982492e-06
    Ans = 3, Time taken = 6.599999999995498e-06        
    Ans = 4, Time taken = 6.899999999997186e-06 '''
    def depth(self, root: treeNode) -> treeNode:
        '''recursive dfs'''
        if not root:
            return 0
        #at each node 1 + no. of levels traversed is returned
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
    
class soln2:
    '''Runtime: 77 ms, faster than 26.57% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 15.2 MB, less than 90.36% of Python3 online submissions for Maximum Depth of Binary Tree. 
    Ans = 2, Time taken = 7.899999999998186e-06
    Ans = 3, Time taken = 8.399999999998686e-06        
    Ans = 4, Time taken = 1.8200000000002936e-05 '''
    def depth(self, root: treeNode) -> treeNode:
        '''iterative dfs'''
        #stack for storing children with which level they are in; init with root and depth 1
        stack  = [[root, 1]]
        max_depth = 0 
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                #append child node with which level they are in
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return max_depth
    
class soln3:
    '''Runtime: 58 ms, faster than 65.63% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 15.2 MB, less than 90.36% of Python3 online submissions for Maximum Depth of Binary Tree.
    Ans = 2, Time taken = 1.0799999999998311e-05
    Ans = 3, Time taken = 1.0699999999995435e-05       
    Ans = 4, Time taken = 1.4600000000003499e-05'''
    def depth(self, root: treeNode) -> treeNode:
        '''bfs'''
        if not root:
            return 0
        depth = 0
        q = deque([root])
        #while loop to traverse til end of tree
        while q:
            #for loop for traversing among a level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #depth incremented only after a level has been traversed by the for loop
            depth += 1
        return depth
        
        
        
tree1 = treeNode(1); tree1.left = treeNode(2)
tree2 = treeNode(1); tree2.left = treeNode(5); tree2.right = treeNode(2); tree2.right.right = treeNode(6)
tree3 = treeNode(1); tree3.left = treeNode(5); tree3.right = treeNode(2); tree3.left.left = treeNode(5)
tree3.left.left.left = treeNode(5)

test = soln1()

start_time = time.perf_counter()
ans = test.depth(tree1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.depth(tree2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.depth(tree3)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")