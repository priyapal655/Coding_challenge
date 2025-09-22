class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_result= {}
        result=[]
        
        for i,num in enumerate(nums):
            check= target-num
            if check in h_result:
                return [h_result[check], i]
            h_result[num]=i
        return []
