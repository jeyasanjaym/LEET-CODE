class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = list(dict.fromkeys(nums))
        k = len(n)
        for i in range(k):
            nums[i] = n[i]

        for i in range(k, len(nums)):
            nums[i] = "_"

        return k


