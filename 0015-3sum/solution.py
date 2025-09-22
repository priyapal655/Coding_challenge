class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right =len(nums)-1
            target = -nums[i]
            while left<right:
                total = nums[left]+nums[right]
                if(total==target):
                    result.append([nums[left],nums[i],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<target:
                    left+=1
                else:
                    right-=1
        return result










        # nums.sort()
        # result = set()
        
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue 
            
        #     target = -nums[i]
        #     seen = set()
        #     j = i + 1
            
        #     while j < len(nums):
        #         check = target - nums[j]
        #         if check in seen:
        #             triplet = tuple([nums[i], nums[j], check])
        #             result.add(triplet)
                
        #         seen.add(nums[j])
        #         j += 1
        
        # return [list(t) for t in result]
