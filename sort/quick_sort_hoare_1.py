"""
quick sort with 
- Hoare Partition
- Divide and Conquer 
- Divide the partition into left and right and iterate scan
"""


def swap(a, b, arr):
    # Method 1
    # arr[a], arr[b] = arr[b], arr[a]

    # Method 2
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    # pivot_index = 0
    pivot_index = start
    pivot = elements[pivot_index]

    # start = pivot_index + 1
    end = len(elements) - 1

    # as long as start is less than end, do this, when start > end, means, start and end has intercepted
    # hence stop.
    while start < end:
        # start pointer if value lesser than pivot - move, else stop (bigger scanner)
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        # end pointer -  if value is bigger than pivot - move , else stop (lower scanner)
        while elements[end] > pivot:
            end -= 1

        # swap the value between start and end
        if start < end:
            swap(start, end, elements)

    # as the previous loop stop, swap the pivot value with end value.
    # pivot is now move forward.
    # as start > end
    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        p_index = partition(elements, start, end)  # initial execution

        """
        p_index now is the the pivot that has been moved to the middle, 
        dividing the list into left and right. 
        
        """
        quick_sort(elements, start, p_index - 1)  # left partition (?)
        quick_sort(elements, p_index + 1, end)  # right partition (?)


if __name__ == "__main__":
    numbers = [3, 4, 10, 6]
    quick_sort(numbers, 0, len(numbers) - 1)
    print(numbers)
