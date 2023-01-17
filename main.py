from __future__ import print_function


def binary_search(arr, key):
    if arr[0] > arr[-1]:
        return binary_search_dec_rec(arr, key, 0, len(arr))
    else:
        return binary_search_acc_rec(arr, key, 0, len(arr))


def binary_search_acc_rec(arr, key, lower, upper):
    if lower > upper or lower == len(arr):
        return -1

    middle = (lower + upper) // 2
    print(middle)

    if arr[middle] == key:
        return middle
    elif arr[middle] < key:
        return binary_search_acc_rec(arr, key, middle + 1, upper)
    else:
        return binary_search_acc_rec(arr, key, lower, middle - 1)


def binary_search_dec_rec(arr, key, lower, upper):
    if lower > upper:
        return -1

    middle = (lower + upper) // 2

    if arr[middle] == key:
        return middle
    elif arr[middle] > key:
        return binary_search_dec_rec(arr, key, middle + 1, upper)
    else:
        return binary_search_dec_rec(arr, key, lower, middle - 1)


def main():
    print(binary_search([-1, 0, 3, 5, 9, 12], 13))
    # print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    # print(binary_search([10, 6, 4], 10))
    # print(binary_search([10, 6, 4], 4))


if __name__ == "__main__":
    main()
