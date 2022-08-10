import time


def non_repeat_substring(str1):
    max_substring_size = 0
    characters = {str1[0]: 0}
    start_pointer = 0
    for i in range(len(str1)):
        characters[str1[i]] = characters.get(str1[i], 0) + 1

        if max(characters.values()) == 1:
            max_substring_size = max(max_substring_size, i - start_pointer + 1)

        while max(characters.values()) > 1:
            if characters.get(str1[start_pointer], 0) > 1:
                characters[str1[start_pointer]] = characters[str1[start_pointer]] - 1
            else:
                characters.pop(str1[start_pointer])

            start_pointer += 1

    return max_substring_size


def length_of_longest_substring(arr, k):
    return 2


def is_contains_unique_char(pattern_dict: dict):
    for count in pattern_dict.values():
        if count > 1:
            return False
    return True


def is_contains_all_pattern(pattern_dict: dict):
    for count in pattern_dict.values():
        if count != 1:
            return False
    return True


def find_permutation(str1, pattern):
    pattern_char_count = {pattern[0]: 0}
    for s in pattern:
        pattern_char_count[s] = pattern_char_count.get(s, 0) + 1

    window_char_count = {str1[0]: 0}
    start_pointer = 0

    for i in range(len(str1)):
        if str1[i] not in pattern:
            start_pointer = i + 1
            window_char_count.clear()
            continue

        window_char_count[str1[i]] = window_char_count.get(str1[i], 0) + 1
        while window_char_count.get(str1[i], 0) > pattern_char_count.get(str1[i], 0):
            window_char_count[str1[start_pointer]] = window_char_count.get(str1[start_pointer], 0) - 1
            start_pointer += 1

        if window_char_count == pattern_char_count:
            return True

    return False


if __name__ == "__main__":
    st = time.time()

    print(find_permutation("ooolleoooleh", "hello"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("odicf", "dc"))
    print(find_permutation("aaacb", "abc"))

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
