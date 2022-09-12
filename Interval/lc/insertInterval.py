class Solution:
    ##not my solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: #not my solution
        for [start, end] in intervals[:]: #get each interval

            if start <= newInterval[0] and end >= newInterval[1]: #if the newInterval is contained within the current interval, then return the intervals, since you dont need to merge nor insert anything. Ex) newInterval = [1, 3], intervals = [[0,5]....]. [1,3] is contained within [0,5] so we can just return
                return intervals

            if newInterval[0] >= start and newInterval[0] <= end: #if the start number for newInterval is contained within an interval, ex) newInterval = [1,7] intervals = [[0,3], [4,5], [9,10]...], 1 is between 0 and 3, then set newInterval[0] = to the smallest number in the interval, which is between newInterval[0] or start, therefore newInterval[0] = 0. Then remove it, so intervals becomes intervals = [[4,5], [9,10], ....]
                newInterval[0] = min(newInterval[0], start)
                intervals.remove([start,end]) #finds array interval with current start and end numbers, and removes it. Even after removing from array, the variables are still stored in start and end, so they can be used after this line, until the end of this current running loop

            if newInterval[1] >= start and newInterval[1] <= end: ## if the newValue end digit is between an interval, say we had [6,8] as an interval in the previous example, and left newInterval = [1,7], then we set the newInterval end digit, to whatever is the max in the interval, which is either the newInterval[1] or the end digit of the interval we are checking, which is the end bit. Therefore, newInterval[1] = 8, and now newInterval = [0,8].
                newInterval[1] = max(newInterval[1], end)
                if intervals: #Here we check if intervals still has a length, and if it does, we remove the interval that has the current start and end. Here, if [6,8] did exist, then we would remove it
                    intervals.remove([start,end])

            if start > newInterval[0] and end < newInterval[1]: #this is the opposite of the first condition, if the current interval is contained in newInterval, ex) say newInterval = [0,6] and intervals[i] = [1,5], then you remove the interval from the intervals array. For our previous example, [4,5] is contained in newInterval = [0,8], so we remove it, and now intervals = [[9,10] ...]
                intervals.remove([start,end])

        for i, [start, end] in enumerate(intervals): #use enumerate to get indexes of array, stored in variable "i", and then the values at the current index, which is always an array containing two values, start and end
            if newInterval[0] <= start: #Checks if newInterval[0] <= start because now that all intervals that contained or were in the range of the original newInterval ([1,7]) are gone, we have to insert newInterval in increasing order
                intervals.insert(i,newInterval)
                break

        if intervals and newInterval[0] > intervals[-1][0]: #if the newInterval start bit is greater than the start bit of the last interval, then append it, because since newInterval went through the for loop above, it's end bit will also be greater than the end bit of the last interval's end bit.
            intervals.append(newInterval)
        if not intervals: #if nothing in intervals then just append
            intervals.append(newInterval)

#Go through again till it makes sense
        return intervals

