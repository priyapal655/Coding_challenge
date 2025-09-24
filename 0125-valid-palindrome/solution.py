class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned+= char.lower()
        if cleaned!= cleaned[::-1]:
            return False
        else:
            return True
        #two pointer
        # left = 0
        # right=len(cleaned)-1

        # while left<right:
        #     if(cleaned[left]!=cleaned[right]):
        #         return False
        #     left+=1
        #     right-=1
        
        # return True
