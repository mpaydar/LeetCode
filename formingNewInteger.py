# Write a program that asks the user for a positive integer n where the right-most digit is not a
# zero. Construct and output the integer whose digits are the reverse of those in n.
# For example, if n has the value 123, then you need to construct the integer 321. Note you are not
# just printing the digits of n in reverse order; you are actually constructing the new integer.
# 123 =


number = int(input("Enter a number"))
factor = 100
new_number = 0
while number != 0:
    d3 = number % 10
    new_number = new_number * 10 + d3
    factor = factor // 10
    print("Current number is: ", number)
    print("Current digit is: ", d3)
    print("New number is: ", new_number)
    number = number // 10

print("The new number is: ", new_number)
