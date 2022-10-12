class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()   # sort the merged array
        length = len(nums1)
        half = length//2
        if(length%2 != 0):
            return nums1[half] # median is the middle number
        else:
            mean = (nums1[half] + nums1[half - 1])/2 # median is the avg. of 2 middle numbers
            return mean
