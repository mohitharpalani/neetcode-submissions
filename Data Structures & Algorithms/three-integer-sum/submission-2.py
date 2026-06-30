class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # ans = set()

        # for i in range(n - 2):
        #     st = set()

        #     for j in range(i + 1, n):
        #         target = -nums[i] - nums[j]

        #         if target in st:
        #             ans.add(tuple(sorted([nums[i], nums[j], target])))

        #         st.add(nums[j])

        # return [list(triplet) for triplet in ans]
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans


            