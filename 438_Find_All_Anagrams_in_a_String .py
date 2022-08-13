def find_string_anagrams(str1, pattern):
    result_indexes = []
    start_pinter = 0
    window_size = len(pattern)
    window_char_count: dict = {str1[0]: 0}
    pattern_char_count = {pattern[0]: 0}
    for s in pattern:
        pattern_char_count[s] = pattern_char_count.get(s, 0) + 1

    for i in range(len(str1)):
        window_char_count[str1[i]] = window_char_count.get(str1[i], 0) + 1

        if i - start_pinter + 1 > window_size:
            if window_char_count.get(str1[start_pinter], 0) > 1:
                window_char_count[str1[start_pinter]] = window_char_count[str1[start_pinter]] - 1
            else:
                window_char_count.pop(str1[start_pinter])
            start_pinter += 1

        if window_char_count == pattern_char_count:
            result_indexes.append(start_pinter)

    return result_indexes
