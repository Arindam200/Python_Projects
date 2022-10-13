class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Edge case: input size too small
        if len(nums) < 3:
            return False
        
        # Search for first increasing pair (pair1, pair2)
        pair1 = min(nums[0], nums[1])
        pair2 = nums[1]
        i = 2
        # While pair is non increasing
        while i < len(nums) and pair1 >= pair2:
            # Found a viable increasing pair
            if nums[i] > pair1:
                pair2 = nums[i]
                break
            # Found a smaller number to use for pair1
            elif nums[i] < pair1:
                pair1 = nums[i]
                pair2 = nums[i]
            i += 1
        
        minNum = pair1
        for n in nums[i:]:
            if pair1 < n and n < pair2:
                # Update pair2
                pair2 = n
            elif minNum < n and n < pair2:
                # Update the full pair
                pair1 = minNum
                pair2 = n
            elif n < minNum:
                # Update the min num
                minNum = n
            elif pair2 < n:
                # Answer found
                return True
            
        return False
