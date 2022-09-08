from ast import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if (len(intervals) == 1 and newInterval[0] > intervals[0][1]) or newInterval[
            0
        ] > intervals[len(intervals) - 1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        start = 0
        end = 0
        while start < len(intervals) and intervals[start][1] < newInterval[0]:
            start += 1
        # start -= 1
        end = start
        while end < len(intervals) and intervals[end][0] < newInterval[1]:
            end += 1

        while start >= len(intervals):
            start -= 1
        while end >= len(intervals):
            end -= 1

        if newInterval[1] < intervals[end][0] and end > 0:
            end -= 1

        c = [
            min(intervals[start][0], newInterval[0]),
            max(intervals[end][1], newInterval[1]),
        ]

        return intervals[:start] + [c] + intervals[end + 1 :]
