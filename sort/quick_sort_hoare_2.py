"""
- Hoare schemes (v2)
- Status: Unsolved (yet)


"""


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, current_index, swap_marker_index):
    pivot = elements[-1]

    while elements[current_index] > pivot:
        current_index += 1

    while elements[current_index] < pivot and swap_marker_index < len(elements) - 1:
        swap_marker_index += 1

    if elements[current_index] < elements[swap_marker_index]:
        swap(current_index, swap_marker_index, elements)


if __name__ == "__main__":
    numbers = [3, 6, 5, 7]
    partition(numbers, 0, 0)
    print(numbers)
