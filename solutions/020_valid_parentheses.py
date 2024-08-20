from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']':'['
        }
        for c in s:
            if c not in mapping.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == mapping[c]:
                    stack.pop()
                else: 
                    return False

        return len(stack) == 0
        