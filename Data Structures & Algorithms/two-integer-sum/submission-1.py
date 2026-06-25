class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce approach
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return -1
        
        mp={}
        for i in range(len(nums)):
            if target-nums[i] in mp:
                complement=target-nums[i]
                return [mp[complement],i]
            else:
                mp[nums[i]]=i
