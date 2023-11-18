def selection_sort(arr):
    size = len(arr)

    for i in range(size - 1):
        min_index = i

        # iterate to get min_index
        # min_index + 1 is next value to min_index
        for j in range(min_index + 1, size):
            print(arr[j], arr[min_index])
            if arr[j] < arr[min_index]:
                # if the j-index value is less than current min_index, swap
                min_index = j
        # optimize
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# --- EXERSICE (done)
# multi-level sort
"""
- Implement multi-level sort
- If user wants to sort dict based on first key "A", then "B", user
will passed list args ["A", "B"]
- Code should be able to sort list of dict, for any numbers of key in sorting order
- For the following case, the user can choose to sort by "First Name" then "Last Name", 
or in vice versa order.
"""


def sort_multi_level(fullname_arr: list[dict[str, str]], key_sort_by: str):
    size = len(fullname_arr)
    for i in range(size - 1):
        min_index = i

        for j in range(min_index + 1, size):
            # print(fullname_arr[j][key_A], fullname_arr[min_index][key_A])
            if fullname_arr[j][key_sort_by] < fullname_arr[min_index][key_sort_by]:
                # print(fullname_arr[j][key_A], fullname_arr[min_index][key_A])
                min_index = j

        if i != min_index:
            fullname_arr[i], fullname_arr[min_index] = (
                fullname_arr[min_index],
                fullname_arr[i],
            )


if __name__ == "__main__":
    # numbers = [12, 222, 1, 3, 4, 55, 64]

    # selection_sort(numbers)
    # print(numbers)

    # -- Exerice
    test_dict = [
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Aahana", "Last Name": "Arora"},
    ]
    sort_multi_level(test_dict, key_sort_by="Last Name")
    print(test_dict)
