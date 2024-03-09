class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1NumFreq = Counter(nums1)
        nums2NumFreq = Counter(nums2)
        
        nums1NumFreqSorted = sorted(nums1NumFreq.items(), key=lambda x:x[0], reverse=True)
        nums2NumFreqSorted = sorted(nums2NumFreq.items(), key=lambda x:x[0], reverse=True)
        
        # Get the min value
        ans = float('inf')
        i = j = 0
        
        while i < len(nums1NumFreqSorted) or j < len(nums2NumFreqSorted):
            # Assign values
            num1 = nums1NumFreqSorted[i] if i < len(nums1NumFreqSorted) else (float('-inf'), float('-inf'))
            num2 = nums2NumFreqSorted[j] if j < len(nums2NumFreqSorted) else (float('-inf'), float('-inf'))
            
            
            if num1[0] in nums2NumFreq: # means it exists
                ans = min(ans, num1[0])

            if num1[0] > num2[0]:
                i += 1
            else:
                j += 1
                
            
        return ans if ans != float('inf') else -1
                
        
        