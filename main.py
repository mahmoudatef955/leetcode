import math
from operator import le
import time
from typing import List


def find_substring(str1, pattern):
    pattern_char_count = {pattern[0]: 0}
    for s in pattern:
        pattern_char_count[s] = pattern_char_count.get(s, 0) + 1

    start_pointer, min_start_pointer, min_window_size = 0, 0, math.inf
    matched_count = 0

    for i in range(len(str1)):
        if str1[i] in pattern:
            pattern_char_count[str1[i]] -= 1
            if pattern_char_count[str1[i]] >= 0:
                matched_count += 1

        while matched_count == len(pattern):
            if i - start_pointer + 1 < min_window_size:
                min_start_pointer = start_pointer
                min_window_size = i - start_pointer + 1

            if str1[start_pointer] in pattern:
                pattern_char_count[str1[start_pointer]] += 1
                if pattern_char_count[str1[start_pointer]] > 0:
                    matched_count -= 1
            start_pointer += 1

    if min_window_size != math.inf and min_window_size > 0:
        return str1[min_start_pointer : int(min_start_pointer + min_window_size)]

    return ""


def find_word_concatenation(str1: str, words: List[str]) -> List[int]:
    result_indices, matched_words = [], []
    start_pointer, word_pointer = 0, 0
    min_word_length = len(min(words, key=len))
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

    for i in range(len(str1)):
        if str1[word_pointer : i + 1] in words:
            w = str1[word_pointer : i + 1]
            if words_count.get(str1[word_pointer : i + 1], 0) > 0:
                words_count[str1[word_pointer : i + 1]] -= 1
                matched_words.append(str1[word_pointer : i + 1])

                if len(matched_words) == len(words):
                    result_indices.append(start_pointer)
                    start_pointer = i + 1
                    # word_pointer = i + 1
                    matched_words.clear()
                    for word in words:
                        words_count[word] = words_count.get(word, 0) + 1

            else:
                # start_pointer = i + 1
                word_pointer = i + 1
                # matched_words.clear()
            word_pointer = i + 1

        elif i - word_pointer + 1 >= min_word_length:
            start_pointer = i + 1
            word_pointer = i + 1
            matched_words.clear()

    return result_indices


if __name__ == "__main__":
    st = time.time()

    # print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
