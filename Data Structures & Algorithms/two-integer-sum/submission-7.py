class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i,n in enumerate(nums):

            required = target -n

            if required in data:
                return [data[required], i]
            data[n] = i