class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i, value in enumerate(nums1):
            for j in nums2[nums2.index(value):]:
                 if j > nums1[i]: # If we find a value greater than it, append and break
                    ans.append(j)
                    break
            else:
                ans.append(-1)
        
        return ans