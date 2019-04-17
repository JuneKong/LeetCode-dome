class Solution:
    # 3Sum:两重遍历+set
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, a in enumerate(nums[:-2]):
            if i >= 1 and a == nums[i - 1]:
                continue
            dict = {}
            for b in nums[i+1:]:
                if b not in dict:
                    dict[-a-b] = 1
                else:
                    res.add((a, -a-b, b))
        return map(list, res)
                
    # 3Sum:一重遍历+两边夹击法
    def SumThree(self, nums):
        if len(nums) < 3:
            return []
        res = []
        nums.sort() # **排序
        for i, a in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l, r = i+1, len(nums)-1
            while l < r:
                target = nums[l] + nums[i] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append((nums[l], nums[i], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                    
        return res

    # 3Sum:运用twoSum
    def threeThreeBy2Sum(self, nums):
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            new = nums[i+1:]
            two_nums = self.twoSum(self, new, -val)
            for two in two_nums:
                res.append([val, new[two[0]], new[two[1]]])
        return res
        
        
    def twoSum(self, nums: 'List[int]', target: 'int'):
        if len(nums) < 2:
            return []
        d = {}
        res = []
        for i in range(len(nums)):
            y = target - nums[i]
            if y in d and d[y] != i:
                res.append([d[y], i])
            d[nums[i]] = i;
        return res


l = [-1, 0, 1, 2, -1, -4]
res = Solution.threeThreeBy2Sum(Solution, l)
print(res)
