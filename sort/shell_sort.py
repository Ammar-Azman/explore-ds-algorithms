def shell_sort(arr):
    # arr = list(set(arr))
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]

            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = anchor

        gap = gap // 2


if __name__ == "__main__":
    numbers = [[13, 12, 65, 41, 3, 2, 6, 5], [], [1, 2, 4, 5, 6], [3, 3, 4, 4, 5, 5]]
    for test in numbers:
        shell_sort(test)
        print(test)

# Exersice
# remove duplicate value
