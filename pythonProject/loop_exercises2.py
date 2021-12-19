#1
for i in range(1,6):
    print(str(i) * i)

"""2. Write a program to check if the given number is a palindrome number. A palindrome number is a number that is 
the same after reverse. For example 545, is the  palindrome number. """

number = input()

number_1 = number[::-1]
if number == number_1:
    print("This number is a palidrone number")
else:
    print("This number isn't a palidrone number")

#OR
number = int(input())
number_1 = number
rev_number = 0
while number > 1:
    res = number % 10
    rev_number = rev_number * 10 + res
    number = number // 10
if number_1 == rev_number:
    print("This number is a palidrone number")
else:
    print("This number isn't a palidrone number")


#3. Write a Program to extract each digit from an integer(e.g. 56743) in the reverse order.
number = 56743
other_number = number
while number > 0:
    res = number % 10
    reverse_number = res * 10
    number = number // 10

#4. Print multiplication table from 1 to 10.
x = input("Please enter a number")
for i in range(1,11):
    print(x +" * "+ str(i) +" = " +str(int(x) * i))

#5. Print downward Half-Pyramid Pattern with Star (asterisk):

for i in range(5,0,-1):
    print("*" * i)

