from ast import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        merged_intervals = []

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        merged_intervals.append([start, end])

        return merged_intervals
