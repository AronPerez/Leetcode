class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, current_sum, combination):
            if current_sum == target:
                result.append(combination.copy())
                return

            if index >= len(candidates) or current_sum > target:
                return

            combination.append(candidates[index])
            backtrack(index, current_sum + candidates[index], combination)
            combination.pop()
            backtrack(index + 1, current_sum, combination)

        backtrack(0, 0, [])

        return result
        