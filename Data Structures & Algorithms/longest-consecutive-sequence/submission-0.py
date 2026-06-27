class Solution:
    
    def longestConsecutive(self, nums):
        longest = 0

        for num in nums:
            current = num
            length = 1

            while True:
                found = False

                for x in nums:
                    if x == current + 1:
                        found = True
                        current += 1
                        length += 1
                        break

                if not found:
                    break

            longest = max(longest, length)

        return longest