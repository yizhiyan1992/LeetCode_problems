import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums == []:
            return []
        n = len(nums)
        new_nums = [None for _ in range(n)]
        for i in range(n):
            new_nums[(i + k) % n] = nums[i]
        nums=copy.copy(new_nums)
        # nums=new_nums (why assgining doesnt work?)