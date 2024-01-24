""" Write a program that swaps the value of avariable a and b .You are not allowed to use a third
variable. you are not allowed to perform arithmatic on a and b"""


def swap_without_temp(a, b):
    print("Before swap: a = {a}, b = {b}")
    #
    # Swapping values without using a third variable or arithmetic operations
    a = a ^ b
    b = a ^ b
    a = a ^ b
    #
    print("After swap: a = {a}, b = {b}")


#
#
# # Example usage
# a = 5
# b = 10
# swap_without_temp(a, b)

a = 23
b = 25
a, b = b, a
print(a)
print(b)
