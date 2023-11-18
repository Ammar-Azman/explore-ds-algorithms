# Big o notation
import time
def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        fun = func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper
    

# Example of O(n)
# - loop on array 
@time_execution
def get_squared(numbers):
    final_value = []
    for num in numbers:
        final_value.append(num*num)
    return final_value

# Example of 0(1)
# - no loop
@time_execution
def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

#  Example of O(n^2)
# - nested loop

# NOTE: Big 0 concept
# 1. Keep only fastest growing term
# 2. Drop constant

# Binary Search - O(log n)
# - Example; find 90 in this list [12,3,34,3,4,33, 90, 123,2,3]
# Psuedocode: 
    # - sort list
    # - divide list by 2, get the value_a
    # - check whether it is less (depends on what we want) than 90 (for example)
    # - if yes, discard the value less than value_a
    # - iterate again, until we get value 90




if __name__ == "__main__":
    print(get_squared([1,2,3,4]))
    print(find_first_pe(prices=[100,200,300],eps=[100,200,330],
                        index=1))
