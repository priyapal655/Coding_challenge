class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        
        def recursive(start):
            if start == len(nums):
                return permutations.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i]= nums[i], nums[start]
                recursive(start +1)
                nums[start], nums[i]= nums[i], nums[start]
        recursive(0)
        return permutations
