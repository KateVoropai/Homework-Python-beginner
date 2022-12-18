def print_all_digits_of_number(number: int) -> int:
    n = len(str(number))
    if n == 1:
        return number
    first_digit = number // 10**(n - 1) 
    print(first_digit)
    return print_all_digits_of_number(number % 10**(n - 1))
            
number = 12345
print(print_all_digits_of_number(number))