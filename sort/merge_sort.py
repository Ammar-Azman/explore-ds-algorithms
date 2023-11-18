def merge_sort(arr):
    """
    Function recursively divide into 2 the array until ends,
    before returning array when the recursive ends
    to the merged_two_sorted_list.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # print(len(arr), mid)
    left = arr[:mid]
    right = arr[mid:]

    # Analysis:
    # every recursion, it creates new arr
    # hence not efficient in terms of complexity
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)


def merge_two_sorted_list(arr_A: list, arr_B: list) -> None:
    sorted_list = []
    len_a = len(arr_A)
    len_b = len(arr_B)

    i = j = 0
    # iterate till the end of the array
    while i < len_a and j < len_b:
        if arr_A[i] <= arr_B[j]:
            sorted_list.append(arr_A[i])
            i += 1
        else:
            sorted_list.append(arr_B[j])
            j += 1

    # handling case of
    # no element of arr_A is bigger than element arr_B
    # but i is not > len_a (end of arr_A)
    while i < len_a:
        sorted_list.append(arr_A[i])
        i += 1
    # handling case of
    # no element of arr_B is bigger than element arr_B
    # but j is not > len_b (end of arr_B)
    while j < len_b:
        sorted_list.append(arr_B[j])
        j += 1

    return sorted_list


if __name__ == "__main__":
    # arr_A = [1, 2, 5, 6]
    # arr_B = [33, 45, 67, 88]

    # sorted_list = merge_two_sorted_list(arr_A, arr_B)
    # print(sorted_list)

    full_arr = [33, 45, 67, 88, 1, 2, 5, 6, 9]
    print(merge_sort(full_arr))
