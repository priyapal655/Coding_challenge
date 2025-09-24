class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesis_pairs = {')':'(','}':'{',']':'['}
        stack= []

        for char in s:
            if char in parenthesis_pairs.values():
                stack.append(char)
            elif char in parenthesis_pairs.keys():
                if not stack or parenthesis_pairs[char]!=stack.pop():
                    return False
        
        return not stack

