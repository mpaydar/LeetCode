# Write a program that asks the user for a positive integer n where the right-most digit is not a
# zero. Construct and output the integer whose digits are the reverse of those in n.
# For example, if n has the value 123, then you need to construct the integer 321. Note you are not
# just printing the digits of n in reverse order; you are actually constructing the new integer.
# 123 =

number = 123
factor = 100
new_number = 0
for i in range(3):
    d3 = number % 10
    number = number // 10
    new_number += d3 * factor          # number * 100 + number *10 + number * 1..... for n
    factor = factor // 10
print(new_number)
