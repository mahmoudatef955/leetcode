import time


def longest_substring_with_k_distinct(str1, k):
    max_substring_length = 0
    start_pointer = 0
    substring_distinct_characters = {str1[0]: 0}
    for i in range(len(str1)):
        substring_distinct_characters[str1[i]] = substring_distinct_characters.get(str1[i], 0) + 1

        if len(substring_distinct_characters.keys()) <= k:
            max_substring_length = max(max_substring_length, i - start_pointer + 1)

        while len(substring_distinct_characters.keys()) > k:

            if substring_distinct_characters.get(str1[start_pointer], 0) > 1:
                substring_distinct_characters[str1[start_pointer]] = substring_distinct_characters[
                                                                         str1[start_pointer]] - 1
            else:
                substring_distinct_characters.pop(str1[start_pointer])

            start_pointer += 1

    return max_substring_length


if __name__ == "__main__":
    st = time.time()
    print("Longest Substring : " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Longest Substring : " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Longest Substring : " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Longest Substring : " + str(longest_substring_with_k_distinct("cbbebi", 10)))
