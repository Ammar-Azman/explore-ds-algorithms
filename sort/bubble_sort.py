from collections import deque


def bubble_sort(numbers: list):
    # OUTER LOOP - for next bubble floating to the top
    for k in range(len(numbers) - 1):
        swapped = False
        print("swapped before", swapped)
        # INNER LOOP - one bubble floating to the top
        for i in range(len(numbers) - 1 - k):
            # print(numbers[i], numbers[i + 1])
            # -k: ignore the last element that already sorted

            # iSwapping algorithm
            if numbers[i] > numbers[i + 1]:
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp
                swapped = True
                print("swapped current", swapped)

        # To increase the efficiency of the algorithm,
        # we set the swapped logic - if all numbers is
        # already sorted, hence break the the inner loop.
        # This will stop it to iterate the next bubble
        # bubble float completed.
        print("swapped finish", swapped)
        if not swapped:  # if swapped == True:
            break  # break for the single bubble


if __name__ == "__main__":
    numbers = [1, 33, 55, 66, 2, 3, 4]
    bubble_sort(numbers)
    print(numbers)
