from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        prices_length = len(prices)
        for i in range(prices_length):
            if prices[i] > min_price:
                continue
            for j in range(i, prices_length):
                if prices[j] - prices[i] > (max_price - min_price):
                    max_price = prices[j]
                    min_price = prices[i]

        return max_price - min_price


if __name__ == "__main__":
    sln = Solution()
    sss = sln.maxProfit([3, 2, 6, 5, 0, 3])
    print(sss)
