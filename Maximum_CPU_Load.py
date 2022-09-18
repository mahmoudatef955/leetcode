from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.start < other.start


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)

    maxLoad = 0
    currentLoad = 0
    jobsHeap = []

    for job in jobs:

        while len(jobsHeap) > 0 and job.start >= jobsHeap[0].end:
            currentLoad -= jobsHeap[0].cpu_load
            heappop(jobsHeap)

        heappush(jobsHeap, job)
        currentLoad += job.cpu_load
        maxLoad = max(maxLoad, currentLoad)

    return maxLoad


def main():
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)]))
    )
