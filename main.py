from __future__ import print_function

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    # result = []
    # start_min_heap = []
    # start_max_heap = []
    # for i in range(len(intervals)):
    #     heappush(start_min_heap, (intervals[i].start, i))
    #
    # for i in range(len(intervals)):
    #     while start_max_heap and -start_max_heap[0][0] >= intervals[i].end:
    #         tmp = heappop(start_max_heap)
    #         heappush(start_min_heap, (-tmp[0], tmp[1]))
    #
    #     while start_min_heap and start_min_heap[0][0] < intervals[i].end:
    #         tmp = heappop(start_min_heap)
    #         heappush(start_max_heap, (-tmp[0], tmp[1]))
    #
    #     if start_min_heap:
    #         result.append(start_min_heap[0][1])
    #     else:
    #         result.append(-1)
    #
    start_max_heap = []
    end_max_heap = []

    start_min_heap = []

    result = [-1 for _ in range(len(intervals))]

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i].start, i))
        heappush(end_max_heap, (-intervals[i].end, i))

    while end_max_heap:
        c = heappop(end_max_heap)

        while start_max_heap and -start_max_heap[0][0] >= -c[0]:
            cc = heappop(start_max_heap)
            heappush(start_min_heap, (-cc[0], cc[1]))

        if start_min_heap and start_min_heap[0][0] >= c[0]:
            x = heappop(start_min_heap)
            result[c[1]] = x[1]

    return result


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


if __name__ == "__main__":
    main()
