class Solution:
    # 移动窗口的最大值
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums: return []
        windows, res = [], []
        for i, v in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= v:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res

    # 移动窗口的最小值
    def minSlidingWindow(self, nums: 'List[int]', k:'int') -> 'List[int]':
        if not nums: return []
        windows, res = [], []
        for i, v in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] >= v:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res

    # 3Sum
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        for i, a in enumerate(nums[nums[:-2]]):
            print(a)
     

list = [1,3,-1,-3,5,3,6,7]
res = Solution.minSlidingWindow(Solution,list,3)
print(res)
l = [-1, 0, 1, 2, -1, -4]
threeSum(l)

