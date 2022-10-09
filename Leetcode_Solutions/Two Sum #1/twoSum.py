def twoSum(self, nums: List[int], target: int) -> List[int]:
	nums_dict = {}
	for i, num in enumerate(nums):
		diff = target - num
		if diff in nums_dict:
			return [nums_dict[diff], i]
		nums_dict[num] = i
