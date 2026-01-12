#Approach
#Sort intervals by starting time.
#Initialize a prev interval.
#Iterate through the intervals:
#If current interval overlaps with prev, merge them by updating the end time.
#Else, add prev to result and update prev.
#After loop ends, add the last prev.



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev =intervals[0]
        merged=[]

        for i in range(1, len(intervals)):
            if intervals[i][0]<=prev[1]:
                prev[1]=max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev=intervals[i]
                
        merged.append(prev)
        return merged