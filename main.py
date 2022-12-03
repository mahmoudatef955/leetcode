from __future__ import print_function


def find_subsets(nums):
    result = [[]]
    added = {}

    nums.sort()

    count = 0
    for index in range(len(nums)):
        subset_l = len(result)
        if index > 0 and nums[index] == nums[index - 1]:
            prev_count = count
            count = 0
            for i in range(subset_l - prev_count, subset_l):
                c = list(result[i])
                c.append(nums[index])
                count += 1
                result.append(c)
        else:
            count = 0
            for i in range(subset_l):
                c = list(result[i])
                c.append(nums[index])
                count += 1
                result.append(c)

    return result


def main():
    # print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


if __name__ == "__main__":
    main()
