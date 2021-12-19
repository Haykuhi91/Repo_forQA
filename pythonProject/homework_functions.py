#1. Write a Python function to multiply all the numbers in a list.
def mult_func(y):
    z = len(y)
    mult = 1
    i = 0
    while i < z:
        mult = mult * y[i]
        i = i + 1
    print(mult)



#2. Write a Python program to reverse a string.
#Sample String: "1234abcd"
#Expected Output: "dcba4321"

def rev_string(y):
    y = y[::-1]
    print(y)


#3. Write a Python function that takes a list and returns a new list with unique
#elements of the first list.
#Sample List :[1,2,3,3,3,3,4,5]
#Unique List :[1, 2, 3, 4, 5]

def unique_list(y):
    x = set(y)
    z = list(x)
    print(z)


#4. Write a Python function that takes a number as a parameter and check the
#number is prime or not. Go to the editor
#Note : A prime number (or a prime) is a natural number greater than 1 and
#that has no positive divisors other than 1 and itself.

def getprime(number):
    y = range(2,100)
    count = 0
    for i in y:
        if number % i == 0 and number != i:
            count = count + 2
            print(i)

        elif number % i == 0 and number == i:
            count = count + 1

    if count > 1:
        print("number is not prime")
    else:
        print("number is prime")



getprime(6723)