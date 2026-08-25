class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i,n in enumerate(data):
            req = target - n  
            if req in data:
                return[data[req],i]
            data[n] = i       
        
        
        data = {}

        for i,n in enumerate(nums):

            required = target -n

            if required in data:
                return [data[required], i]
            data[n] = i