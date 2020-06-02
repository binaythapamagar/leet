class solution(object):
    
    #removes duplicate element from sorted list by simply iterating via the list and comparing adjacent
    #returns the length of sorted non-duplicate elements in list
    #time complexity o(n)
    def removeRepeatedElement(self, sortedList):
        if(len(sortedList) == 0):
            return 0
        length = 0
        for element,adjacentElement in zip(sortedList,sortedList[1:]):
            if(element == adjacentElement):
                continue
            length += 1
        return length+1
    
if __name__ == "__main__":
    s = solution()
    print(s.removeRepeatedElement([1,2,2,3,4,4]))