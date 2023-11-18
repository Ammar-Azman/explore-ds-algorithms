def time_it(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        y = func(*args, **kwargs)
        end = time.time()
        return f"Execution time: {(end - start)*(1**6)} micro seconds"

    return wrapper


@time_it
def linear_search(num_list, num_to_find):
    for idx, element in enumerate(num_list):
        if element == num_to_find:
            return idx

    return -1


# @time_it
def binary_search(num_list, num_to_find) -> int:
    """
    Because binary search has the concept of
    dividing the list iteratively, hence
    we need to use the concept of left and right index.

    Assumtion: List is sorted.

    Return:
        * index; -1 if not found

    """
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0

    # Iterative method
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = num_list[mid_index]

        if mid_number == num_to_find:
            return mid_index

        if mid_number < num_to_find:
            # Update left index
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1


# @time_it
def binary_search_recursion(num_list, num_to_find, left_index, right_index):
    # Guard clause
    if right_index < left_index:
        return -1  # not found

    # Guard clause
    if num_to_find >= right_index:
        return -1

    # Base case
    mid_index = (left_index + right_index) // 2
    mid_number = num_list[mid_index]

    if mid_number == num_to_find:
        return mid_index  # exit

    if mid_number < num_to_find:
        # Update left index
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    # recurse
    return binary_search_recursion(num_list, num_to_find, left_index, right_index)


def binary_search_recurrence(num_series, num_to_find):
    index = binary_search(num_series, num_to_find)
    all_index = [index]

    # Find the occurence based on the index as the benchmark
    counter = index - 1
    while counter >= 0:
        if num_series[counter] == num_to_find:
            all_index.append(counter)
        else:
            pass
        counter = counter - 1

    counter = index + 1
    while counter < len(num_series):
        if num_series[counter] == num_to_find:
            all_index.append(counter)
        else:
            pass
        counter = counter + 1

    return sorted(all_index)


if __name__ == "__main__":
    num_series = [10, 20, 30, 10, 40, 50, 10, 123, 10]
    big_guy = [x for x in range(1_000_001)]

    # print(linear_search(big_guy, 1_000_000))
    # print(binary_search(big_guy, 1_000_000))
    # print(binary_search_recursion(big_guy, 1_000_001, 0, len(big_guy)))

    # EXERSICE 1
    # Because the number is not sorted.

    # EXERSICE 2
    print(binary_search_recurrence(num_series, 10))
