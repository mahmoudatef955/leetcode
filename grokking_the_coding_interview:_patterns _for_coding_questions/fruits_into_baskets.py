def fruits_into_baskets(fruits):
    max_substring_size = 0
    trees = {fruits[0]: 0}
    start_pointer = 0
    for i in range(len(fruits)):
        trees[fruits[i]] = trees.get(fruits[i], 0) + 1

        if len(trees.keys()) <= 2:
            max_substring_size = max(max_substring_size, i - start_pointer + 1)

        while len(trees.keys()) > 2:
            if trees.get(fruits[start_pointer], 0) > 1:
                trees[fruits[start_pointer]] = trees[fruits[start_pointer]] - 1
            else:
                trees.pop(fruits[start_pointer])

            start_pointer += 1

    return max_substring_size


if __name__ == "__main__":
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
