from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        What does inorder tell us? Postorder?
        - Inorder: Given the root, it indicates the separation between L and R subtrees. 
        But we do not know sequence, see example below. Different ordering, same result from preorder traversal.
                    1
            2               3
        4       5       6       7
        In: [4, 2, 5, 1, 6, 3, 7]
        Post: [4, 5, 2, 6, 7, 3, 1]
                        1
            4                       3
               2                6       7
                    5
        In: [4, 2, 5, 1, 6, 3, 7]
        Post: [5, 2, 4, 6, 7, 3, 1]

        - Postorder: The last node value in each L and R subtree represents the root of the subtree.
                    
        Given last root 1 in Post, separation in In is [4, 2, 5] and [6, 3, 7].
        For the 2 given sizes of 3, L and R of Post are [5,2,4] and [6,7,3]. 
        [4] and [3] are the subtree roots.
        """
        lookup = {y:x for x,y in enumerate(inorder)}
        def buildFromInAndPost(in_start, in_end, post_start, post_end):
            if in_end < in_start: return None
            root = TreeNode(postorder[post_end])
            idx = lookup[root.val]
            left_size = idx - in_start
            root.left = buildFromInAndPost(
                in_start, 
                idx-1, 
                post_start, 
                post_start + left_size - 1,
            )
            root.right = buildFromInAndPost(
                idx + 1, 
                in_end, 
                post_start + left_size, 
                post_end-1,
            )
            return root

            # if not inorder: return None
            # root = TreeNode(postorder[-1])
            # idx = inorder.index(postorder[-1])
            # left = inorder[:idx]
            # right = inorder[idx+1:]
            # root.left = buildFromInAndPost(left, postorder[:len(left)])
            # root.right = buildFromInAndPost(right, postorder[len(left):-1])
            # return root
        
        return buildFromInAndPost(0, len(inorder)-1, 0, len(postorder)-1)
        