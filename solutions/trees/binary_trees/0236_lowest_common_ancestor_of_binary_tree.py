# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Intuition: The node can be anywhere in tree, then we have some cases:
        - in different subtree
        - in same subtree
        """
        def find_lca(node, p, q):
            #print("Call for:", node.val) if node else print(None)
            if not node:
                return None
            if node == p or node == q:
                return node

            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)
            
            # print("Back to Call for:", node.val)
            # print("L:", left.val) if left else print("L: NULL")
            # print("R:", right.val) if right else print("R: NULL")

            if left and right:
                return node 
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        
        if root:
            return find_lca(root, p, q)
        


        