# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a bigger number: "))

if  num1 >= num2:
    print("The second number should be bigger")
else:
    for i in range(num1, num2):
        print(i)