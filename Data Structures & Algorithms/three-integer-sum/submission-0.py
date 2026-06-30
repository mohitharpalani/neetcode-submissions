class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        for i in range(n - 2):
            st = set()

            for j in range(i + 1, n):
                target = -nums[i] - nums[j]

                if target in st:
                    ans.add(tuple(sorted([nums[i], nums[j], target])))

                st.add(nums[j])

        return [list(triplet) for triplet in ans]