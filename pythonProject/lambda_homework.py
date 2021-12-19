#1. Write a Python program to create a lambda function that adds 10 to a given number passed in as an argument
y = lambda x: x + 10
print(y(5))

#2. Create a lambda function that multiplies argument x with argument y and print the result.
a = lambda x,y: x * y
print(a(5,7))

#3. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an
# unknown given number.
def func(x):
    return lambda y: x * y
result = func(7)
fin_result = result(4)
print(fin_result)

#4. Write a Python program to filter a list of odd numbers using Lambda.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x%2!=0, nums))
print(odd_numbers)