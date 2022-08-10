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
