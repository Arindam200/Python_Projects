class Solution:
    def removeDuplicates(self, nums) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
                
        return slow+1


s = Solution()
print(s.removeDuplicates([1,1,2]))
