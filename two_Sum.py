# 21/10/2026
#Time: O(n^2)
#Space: O(1)

from typing import List
class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        n = len (nums)
        for i in range (n):
            for j in range (i+1, n):
                if (nums[i] + nums[j]==target):
                    return [i, j]
        return []

n = int(input("Nhap do dai chuoi: "))
nums = []
for i in range (n):
    nums.append(int(input(f"Phan tu thu {i+1}: ")))
target = int(input("Gia tri target: "))
sol = Solution()
res = sol.twoSum(nums, target)
print(res)