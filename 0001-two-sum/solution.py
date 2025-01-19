class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            solution = []
            add_num = target - i
            try:
                index = nums.index(add_num, nums.index(i)+1)
            except ValueError:
                continue
            if (nums.index(i)!= index):
                if (i + nums[index] == target):
                    solution.append(nums.index(i))
                    solution.append(index)
                    break
        return solution
        
