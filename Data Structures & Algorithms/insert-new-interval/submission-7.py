class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval

        result = []
        searching = True
        for interval in intervals:
            if searching and interval[0] > new_start:
                result.append(newInterval)
                searching = False
            result.append(interval)
        if searching:
            result.append(newInterval)
         
        print(f'inserted {result}')
        smoothed = []
        for interval in result:
            start, end = interval
            if smoothed and end <= smoothed[-1][1]:
                continue
            elif smoothed and start <= smoothed[-1][1] < end:
                smoothed[-1][1] = end
            else:
                smoothed.append(interval)
        print(f'smoothed {smoothed}')

        return smoothed