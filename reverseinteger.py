class solution(object):
    
    def reverseInteger(self,value):
        if(value < 0):
            return False

        reverse = 0
        while(value != 0):
            print(value)
            reverse = reverse*10 + value % 10
            value = int(value / 10)
        
        return reverse
    
if __name__ == "__main__":
    s = solution()
    print(s.reverseInteger(123))        