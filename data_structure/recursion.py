"""
# Recursion
- Base condition  (exit)
"""


def find_sum(x):
    # --------- recursive started -------------
    if x == 1:
        print(f"{x} == 1, exit")
        return 1  # base/exit

    new_x = x - 1  # recursive execution
    current_total = x + find_sum(new_x)
    # --------- recursive ended -------------

    # -------- this line will be execute after recursive process ended ----

    # value will be printed after the stack unwinding
    print(f"{x} + {new_x} == {x + new_x}")

    return current_total  # recursive function return


def fibon_total(n):
    # ------------ recursive start ---------
    if n == 0 or n == 1:  # base case
        return n
    print("call")
    start = fibon_total(n - 1)  # recursive
    print("call_2")
    end = fibon_total(n - 2)  # recursive

    # --------- recurseve 1 ended ----------
    return start + end  # recursive return


# --------------------- EXERSICE w3resource -------------------
def calc_sum_series(num_series: list):
    len_ = len(num_series)
    if len_ == 1:
        return num_series[0]

    else:
        return num_series[0] + calc_sum_series(num_series[1:])


if __name__ == "__main__":
    # print(find_sum(5))
    print(fibon_total(10))

    # print(calc_sum_series([1, 2, 3, 4]))
