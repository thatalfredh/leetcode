from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Since inorder traversal of a BST is sorted order, 
        we just need to traverse in order for both trees and compare their values
        """
        # arr = []
        # def traverse_inorder(node, arr):
        #     if not node: return None
        #     traverse_inorder(node.left, arr)
        #     arr.append(node.val)
        #     traverse_inorder(node.right, arr)
        # traverse_inorder(root1, arr)
        # traverse_inorder(root2, arr)
        # arr.sort()
        # return arr

        arr1 = []
        arr2 = []
        stack1 = deque([])
        stack2 = deque([])
        def iterative_inorder(node, stack, arr):
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                arr.append(node.val)
                node = node.right
            return
        iterative_inorder(root1,stack1,arr1)
        iterative_inorder(root2,stack2,arr2)
        res = []
        l1, l2 = len(arr1), len(arr2)
        i, j = 0,0
        while i < l1 or j < l2:
            if i >= l1:
                res.append(arr2[j])
                j += 1
            elif j >= l2:
                res.append(arr1[i])
                i += 1
            elif arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        return res