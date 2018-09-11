class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		res = nums[0] + nums[1] + nums[2]
		closest = abs(nums[0] + nums[1] + nums[2] - target)
		for i in range(len(nums)-2):
			if closest == 0:
				break
			if nums[i] > target/3:
				break
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, len(nums)-1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				temp = abs(s - target)
				if temp < closest:
					res = s
					closest = temp
				if s > target:
					r -= 1
				elif s < target:
					l += 1
				else:
					break
		return res

a = Solution()
out = a.threeSumClosest([-1,-2,0,4,2,1,-1],10)
print(out)

