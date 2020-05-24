class Solution(object):
    
    def romantoInteger(self,value):
        romans = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total,previous = 0,0
        for x in value:
            curr = romans[x]
            total += curr
            if curr > previous:
                total -= 2 * previous 
            previous = curr
            
        return total
    
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.romantoInteger('CCC'))