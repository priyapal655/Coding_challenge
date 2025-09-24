class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # char_set = set()
        # left, max_lenght =  0, 0

        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left+=1
            
        #brute force
        max_length = 0
        seen = {}
        left = 0
        #substring_array= []
        for i,char in enumerate(s):
            if char in seen and seen[char] >= left:
                left= seen[char]+1
            seen[char]= i
            if(max_length < i-left+1):
                max_length = i-left+1
        return max_length
                

        # for i,sub in enumerate(substring_array):
        #     sub_set = set(sub)
        #     if(len(sub)!= len(sub_set)):
        #         continue
        #     elif max_lenght < len(sub):
        #         max_lenght = len(sub)
        # return max_lenght




