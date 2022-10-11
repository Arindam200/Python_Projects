# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target
#Find all unique quadruplets in the array which gives the sum of target.
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


def fourSum(nums: List[int], target: int) -> List[List[int]]:
   
    quadruplets = list()
   
    if nums is None or len(nums) < 4:
        return quadruplets
   
    nums.sort()
   
    n = len(nums)
    
    for i in range(0, n - 3):
       
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
           
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
           
            k = j + 1
            l = n - 1
           
            while k < l:
                current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if current_sum < target:
                    k += 1
                elif current_sum > target:
                    l -= 1
                else:
                    quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return quadruplets
