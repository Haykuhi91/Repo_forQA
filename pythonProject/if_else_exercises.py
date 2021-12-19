#Optional task: Ask user to input a , b , c , d values (research how to  do this)
a = input()
b = input()
c = input()
d = input()


#1. Print "Hello World" if a is greater than b.
if a > b:
    print("Hello World")

#2. Print "Yes" if a is equal to b, otherwise print "No".
if a == b:
    print("Yes")
else:
    print("No")

#3. Put the previous 2 statements in one line
if a > b:
    print("Hello World")
elif a == b:
    print("Yes")
else:
    print("No")

#4. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise  print "3"
if a == b:
    print(1)
elif a > b:
    print(2)
else:
    print(3)

#5. Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
    print("Hello")

#6. Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
    print("Hello")

