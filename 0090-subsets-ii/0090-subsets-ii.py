class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, subset):
            result.append(subset.copy())

            for i in range(index, len(nums)):
                # Skip duplicate elements
                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])

        return result
        