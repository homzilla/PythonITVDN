def print_sum(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sum func must be ints')
    print(num1 + num2)


print_sum(1, 'hi')
print_sum(2, 3)

