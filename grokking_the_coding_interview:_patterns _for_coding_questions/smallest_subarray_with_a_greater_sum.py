import math


def smallest_subarray_sum(s, arr):
    min_size = math.inf
    start_pointer = 0
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        while window_sum >= s:
            min_size = min(min_size, (i - start_pointer + 1))
            window_sum -= arr[start_pointer]
            start_pointer += 1

    if min_size == math.inf:
        return 0
    return min_size

# if __name__ == '__main__':
#     print(smallest_subarray_sum(8, [3, 4, 1, 1, 6]))
