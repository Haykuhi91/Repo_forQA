#Exercise 1: Write a program to create a function that takes two arguments, name  and age, and print their value.
def name_age(name,age):
  print(name,age)


#Exercise 2: Write a program to create function func1() to accept a variable length of  arguments and print their value.

def func1(*arg):
    print(*arg)

y = ["a", "b", "d"]
func1(y)

"""Exercise 3: Write a program to create function calculation() such that it can accept  two variables and calculate addition
 and subtraction. Also, it must return both  addition and subtraction in a single return call."""

def my_func(x,y):
    add = x + y
    sub = x - y
    return(add, sub)


"""Exercise 4: Write a program to create a function show_employee() using the  following conditions.
It should accept the employee’s name and salary and display both. If the salary is missing in the function call
then assign default value 9000 to  salary."""

def show_employee(employee_name, salary = 9000):
    print("employee: ", employee_name)
    print("salary: ", salary)

"""Exercise 5:  
Create an outer function that will accept two parameters, a and b Create an inner function inside an outer function that will calculate the addition of a  and b 
At last, an outer function will add 5 into addition and return it
"""
def func(a,b):
    def func2(a,b):
        return  a + b
    res = func2(a,b) + 5
    return res





