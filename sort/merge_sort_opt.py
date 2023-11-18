def merge_sort(arr):
    """
    Function recursively divide into 2 the array until ends,
    before returning array when the recursive ends
    to the merged_two_sorted_list.

    (Complexity optimized version)
    """

    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    # print(len(arr), mid)
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)  # update left
    merge_sort(right)  # update right

    return merge_two_sorted_list(left, right, arr)


def merge_two_sorted_list(arr_A: list, arr_B: list, shorted_arr: list) -> None:
    # sorted_list = [] # to remove the execution of producing new arr every divide
    len_a = len(arr_A)
    len_b = len(arr_B)

    i = j = k = 0
    # iterate till the end of the array
    while i < len_a and j < len_b:
        if arr_A[i] <= arr_B[j]:
            shorted_arr[k] = arr_A[i]
            # sorted_list.append(arr_A[i])
            i += 1
        else:
            shorted_arr[k] = arr_B[j]
            # sorted_list.append(arr_B[j])
            j += 1
        k += 1
    # handling case of
    # no element of arr_A is bigger than element arr_B
    # but i is not > len_a (end of arr_A)
    while i < len_a:
        shorted_arr[k] = arr_A[i]
        i += 1
        k += 1
    # handling case of
    # no element of arr_B is bigger than element arr_B
    # but j is not > len_b (end of arr_B)
    while j < len_b:
        shorted_arr[k] = arr_B[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # arr_A = [1, 2, 5, 6]
    # arr_B = [33, 45, 67, 88]

    # sorted_list = merge_two_sorted_list(arr_A, arr_B)
    # print(sorted_list)

    test_arr = [[33, 45, 67, 88, 1, 2, 5, 6, 9], [], [1, 2, 3]]
    for test in test_arr:
        merge_sort(test)
        print(test)
