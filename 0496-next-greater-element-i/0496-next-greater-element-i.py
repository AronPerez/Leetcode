class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i, value in enumerate(nums1):
            for j in range(nums2.index(value), len(nums2)):
                 if nums2[j] > nums1[i]: # If we find a value greater than it, append and break
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        
        return ans