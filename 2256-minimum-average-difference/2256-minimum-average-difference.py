class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        right = sum(nums[1:])
        n = len(nums)
        smallest = abs(left - int(right/(n-1))) if n - 1 != 0 else int(abs(left))

        for i in range(1, n):
            left += nums[i]
            right -= nums[i]

            left_count = i + 1
            right_count= n - left_count
            diff = abs(int((left/left_count)) - int(right/right_count)) if right_count != 0 else abs(int((left/left_count)))

            if diff < smallest:
                smallest = diff
                ans = i
        return ans
