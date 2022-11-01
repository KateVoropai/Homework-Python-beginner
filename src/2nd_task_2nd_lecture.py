def swap_the_values(a, b):
    a, b = b, a
    return f"a = {a}, b = {b}"


a = input()
b = input()
print(swap_the_values(a, b))
