from ast import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        intersections = []
        secondListPointer = 0
        firstListPointer = 0

        while firstListPointer < len(firstList) and secondListPointer < len(secondList):
            x = max(firstList[firstListPointer][0], secondList[secondListPointer][0])
            y = min(firstList[firstListPointer][1], secondList[secondListPointer][1])
            if y >= x:
                intersections.append([x, y])

            if y >= firstList[firstListPointer][1]:
                firstListPointer += 1
            if y >= secondList[secondListPointer][1]:
                secondListPointer += 1

        return intersections
