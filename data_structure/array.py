# memory address is how the location is addressed in list
# bits, bytes
# number is kept in 4 bytes, 1 bytes has 8 bits


# accessing value in list (slicing) - Lookup by index big-o -- O(1)
# looping in list - O(n)
# list.insert(1, 234) -- O(n)
# list.remove(1) -- O(n)

# --- List is dynamic array (Python)
# the properties of list is changeable
# allocate initial capacity in memory
# geometric progression - how the array can handle of new insertion
# Python can mixed the type of element within the array

# ---- Static array (ie; Java)
# Fix sized, allocated to memory with that particular size
#  cannot mix the element type (string, int) together in array

# EXERSICE

# 1. 
my_expenses = [2200, 2000, 2000, 2130, 2190]
print(f"February expense: {my_expenses[1]}")
def total_expense(expenses:list):
    total = 0
    for exp in expenses:
        total += exp
    return total
print(f"Total expense first qquarter: {total_expense(my_expenses[0:4])}")
def find_two_k(expenses):
    check_if_spend = []
    for idx, exp in enumerate(expenses):
        if exp == 2000:
            check_if_spend.append(True)
            print(f"You have spent 2000 in month {idx+1}")
        else:
            pass
    return any(check_if_spend)
    
print(f"Find 2k status: {find_two_k(my_expenses)}")
my_expenses.insert(5, 1980)
print(f"New expenses on June: {my_expenses[5]}")
my_expenses.remove(2130)
my_expenses.insert(3, 2130-400)
print(f"Expense on April after refund: {my_expenses[3]}")


# 2. 
heros = ["spider man", "thor", "hulk", "ironman", "captain america"]
print(f"Length of the list {len(heros)}")

heros.append("black panther")
print(f"New list after adding Black Panter: {heros}")

heros.remove("black panther")
heros.insert(3, "black panther")
print(f"New list after remove and add: {heros}")

heros[1:3] = ["doctor strange"]
print("No hulk and thor", heros)

heros.sort()
print(heros)


