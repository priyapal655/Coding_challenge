class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        self.dfs(nums, [], permutations)
        return permutations
    
    def dfs(self, nums, path, permutations):
        if not nums:
            permutations.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], permutations)
