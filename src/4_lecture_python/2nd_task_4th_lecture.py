def print_number_in_reverse_order(number: int) -> int:
    n = len(str(number))
    if n == 1:
        return number
    print(f"{number % 10}", end = '')
    return print_number_in_reverse_order(number // 10)
            
number = int(input())
print(print_number_in_reverse_order(number))