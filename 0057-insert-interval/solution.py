class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        num_of_intervals = len(intervals)
        result = []
        i=0
        #start
        while i< num_of_intervals and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i=i+1

        #merge
        while i<num_of_intervals and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i=i+1
        result.append(newInterval)
        
        #end
        while i<num_of_intervals and intervals[i][0] > newInterval[1]:
            result.append(intervals[i])
            i=i+1
        
        return result
