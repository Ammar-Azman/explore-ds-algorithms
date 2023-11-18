# THREADING

import threading
import time


def square_num(vals: list):
    for val in vals:
        time.sleep(0.2)  # aritficial delay
        print(f"Squaring - {val}", val**2)


def cube_num(vals: list):
    for val in vals:
        time.sleep(0.2)  # aritficial delay
        print(f"Cubing - {val}", val**3)


arr = [1, 2, 3, 4, 5]

t1 = threading.Thread(target=square_num, args=(arr,))
t2 = threading.Thread(target=cube_num, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
