def foo(x: int) -> int:
    return x*2

def bar(my_list: list[int], i : int):
    if 0 <= i < len(my_list):
        return my_list[i]
    else:
        return None


val1 = foo("hello")
print(val1)

val2 = bar([5,7,3], -2)
print(val)