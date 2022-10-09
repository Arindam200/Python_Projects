def maxArea(self, height: List[int]) -> int:
	start = 0
	end = len(height) - 1
	maxArea = 0
	while start < end:
		currArea = end - start
		if height[start] < height[end]:
			currArea *= height[start]
			start += 1
		else:
			currArea *= height[end]
			end -= 1
		if maxArea < currArea:
			maxArea = currArea

	return maxArea
