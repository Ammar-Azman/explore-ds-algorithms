"""
NOTE
- multiple execution from python exe
- 

"""

import multiprocessing
import time

square_val = []


def square_num(vals: list):
    for val in vals:
        time.sleep(0.2)  # aritficial delay
        print(f"Squaring - {val}", val**2)
        square_val.append(val**2)
        # because we apply multiprocessing,
        # every process has its own address space
        # it means `square_val` has its own address space,
        # where it is global state which
        # does not mix up with the function state


def cube_num(vals: list):
    for val in vals:
        time.sleep(0.5)  # aritficial delay
        print(f"Cubing - {val}", val**3)


arr = [1, 3, 44, 55]
p1 = multiprocessing.Process(target=square_num, args=(arr,))
p2 = multiprocessing.Process(target=cube_num, args=(arr,))


p1.start()
p2.start()

p1.join()
p2.join()

print("Finished")
print(square_val)
