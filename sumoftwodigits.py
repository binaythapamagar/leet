class Solution(object):
    
    #returns keys of two digit who's sum is eqaul to target
    def twosum(self,nums,target):
                
        for value in nums:
            complement = target - value
            if(complement in nums):
                if( nums.index(complement) != nums.index(value)):
                   return (nums.index(complement), nums.index(value))
            
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.twosum([1,2,3,4,7],6))
    