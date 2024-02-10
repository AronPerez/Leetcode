class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k # 0, 5

        # Binary search
        while left < right:  
            mid = (left + right) // 2 # 0 + 5 / 2 = 2, 0 + 2/2 = 1
          # if our element at mid + k is closer to x, we can move the left pointer
            if x - arr[mid] > arr[mid + k] - x: # 4 - 3 > 6 - 4/4-2 > 5 - 4
                left = mid + 1 # 2
            else: # if our element at the mid is closer to x, we can move the right pointer
                right = mid # 2

        #[1, 2, 3, 4, 5, 6, 7, 8]
        # l, r = 2
        # 2 -> 5
        return arr[left:right + k] # [3, 4, 5]
        