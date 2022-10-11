#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

#Return the sum of the three integers.

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

def threeSumClosest(self, nums: List[int], target: int) -> int:        
        diff = float('inf')
        nums.sort()
        for i, num in enumerate(nums):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = num + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
                
        return target - diff
