class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)  # Convert nums1 to a set to remove duplicates and optimize lookup
        result = set()  # Create an empty set to store the intersection

        for num in nums2:  # Iterate through each element in nums2
            if num in set1:  # Check if the element exists in set1
                result.add(num)  # If it exists, add it to the result set

        return list(result)  # Convert the result set to a list and return it
