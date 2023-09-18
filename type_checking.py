"""
Module: type_checking

A instructional module to illuminate type hints.

Author: Dr. Sat Garcia (sat@sandiego.edu)
"""

# add imports after this line

def loyd(x: int) -> int:
    return x*2

def anya(my_list: list[int], i : int):
    if 0 <= i < len(my_list):
        return my_list[i]
    else:
        return None


val1 = loyd("yor")
print(val1)

val2 = anya([5,7,3], -2)
print(val)
