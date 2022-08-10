def length_of_longest_substring(arr, k):
    start_pointer = 0
    window_size = 0
    window_zeros_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            window_size = max(window_size, i - start_pointer + 1)
        else:
            window_zeros_count += 1
            if window_zeros_count <= k:
                window_size = max(window_size, i - start_pointer + 1)
            else:
                while window_zeros_count > k:
                    if arr[start_pointer] == 1:
                        start_pointer += 1
                    else:
                        window_zeros_count -= 1
                        start_pointer += 1

                window_size = max(window_size, i - start_pointer + 1)

    return window_size
