#1. Write a python program to display the given integer in  reverse manner

number = int(input("Enter a number"))
reverse_number = 0

while number > 1:
    dig = number % 10
    reverse_number = reverse_number * 10 + dig
    number = number // 10
print(reverse_number)

#2. Python program to find the circumference and area of a  circle with a given radius

r = float(input("Enter a radius of circle"))
PI = 3.14
circumference = 2 * PI * r
area = PI * r ** 2
print(circumference)
print(area)

#3. Python program to convert the temperature in degree  centigrade to Fahrenheit

Celsius = float(input("Enter the temperature in Celsius"))
Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)