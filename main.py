from __future__ import print_function

from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minHeapCapital = []
    maxHeapProfit = []

    for i in range(len(capital)):
        heappush(minHeapCapital, (capital[i], i))

    for i in range(numberOfProjects):
        while minHeapCapital and minHeapCapital[0][0] <= initialCapital:
            c = heappop(minHeapCapital)
            heappush(maxHeapProfit, -profits[c[1]])

        initialCapital += -heappop(maxHeapProfit)

    return initialCapital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


if __name__ == "__main__":
    main()
