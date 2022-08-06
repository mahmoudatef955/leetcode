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


if __name__ == "__main__":
    st = time.time()
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

    et = time.time()
    elapsed_time = et - st
    print('\nExecution time :', elapsed_time, 'seconds')
