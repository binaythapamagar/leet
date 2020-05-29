class Solution(object):
    
    def searchPosition(self,values,search):
        l = len(values)-1
        i = 0

        while i <= l:
            mid = int (i + (l-1)/2)
            if values[mid] == search:
                return mid
            elif values[mid] > search:
                l = mid-1
            else:
                i = mid+1
        return i

if __name__ == '__main__':
    s = Solution();
    print(s.searchPosition([1,2,5,7,9,21],9))