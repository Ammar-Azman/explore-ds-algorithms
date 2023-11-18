def insertion_sort(elements):
    """
    Pseudocode:
    for every index in the elements:
        anchor = elements[index]

        j = index minus one
        as long as j is bigger than equal to 0 and \
            current anchor is less than previous element to anchor:

            copy the previous elements(j) to one steps forward elements(j+1)
            j = minus current j

        if anchor is bigger than current elements:
            one steps forward elements value is anchor value
            hence swap
            


    """

    for i in range(1, len(elements)):
        anchor = elements[i]
        # print("anchor: ", anchor)
        j = i - 1
        # j would be the index before the anchor
        # print("j-index: ", j)
        # print("j-elem: ", elements[j])
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            # copy the previous elements to one steps forward
            # print("Copy in loop: ", elements)
            j = j - 1  # to ensure the elements check is always behind the anchor
        elements[j + 1] = anchor
        # print("Copy the anchor: ", elements, "\n")


if __name__ == "__main__":
    # numbers = [11, 3, 4, 55, 2]
    # insertion_sort(numbers)
    # print(numbers)
    test_numbers = [[11, 2, 3, 3, 4], [], [2, 1]]
    for i in test_numbers:
        insertion_sort(i)
        print(i, "\n")

    """
    NOTE: Exercise is not done yet.
    """
