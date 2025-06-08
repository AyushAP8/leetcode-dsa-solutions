class treeNode:
    def __init__(self, val = None):
        if val != None:
            self.val = 0
        else:
            self.val = val
        self.left = None
        self.right = None
        
    def __repr__(self):
        return ' '.join(str(v) for v in [self.val, self.left.val, self.right.val])
    
class tree:
    def __init__(self, nodes: list[int]):
        self.head = None
        for i, val in enumerate(nodes):
            if i == 0:
                node = treeNode(val)
                self.head = node
            elif i != (len(nodes) - 1):
                if nodes[i] and val < nodes[i + 1]:
                    node.left = treeNode(val) 
                elif nodes[i] and val > nodes[i + 1]:
                    node.right = treeNode(val)
                    
    def __repr__(self):
        node = self.head
        print(node)
        nodes = []
        while node and (node.left or node.right):
            left, right = node.left, node.right
            nodes.append(node.val, left.val, right.val)
            left, right = node.left, node.right
        return '->'.join(str(n) for n in nodes)
        
                    
tree = tree([1, 2, 3])
print(tree)

