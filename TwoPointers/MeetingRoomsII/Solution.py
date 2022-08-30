class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        time = {}
        for interval in intervals:
            start,end = interval
            if start not in time:
                time[start] = 0
            if end not in time:
                time[end] = 0
            
            time[start] =time[start] +  1
            time[end] = time[end] - 1
            
            
        
        startAndEndTimes = [(key,value) for  key,value in time.items()]
        startAndEndTimes.sort()
        
        
        maxRequired = -float(inf)
        count = 0
        for interval in startAndEndTimes:
            count += interval[1]
            maxRequired = max(maxRequired,count)
            
        return maxRequired
            