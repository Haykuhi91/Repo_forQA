#1. Print First 10 natural numbers using while loop.
i = 1
while i <= 10:
    print(i)
    i = i + 1

#2. Calculate the sum of all numbers from 1 to a 555.
i = 1
sum = 0
while i <= 555:
    sum = sum + i
    i = i + 1
print(sum)

#3. Display numbers from a my_list = [10, 20, 30, 40, 50] list using loop.
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print(i)

#4. Count the total number of digits in the n = 257569 number.
n = 257569
new_n = str(n)
count = 0
for i in new_n:
    count = count  + 1
print(count)

#5. Use a loop to display elements from a given list present at odd index positions: my_list =  [10, 20, 30, 40, 50, 60, 70, 80, 90]
my_list =  [10, 20, 30, 40, 50, 60, 70, 80, 90]
count = len(my_list)
i = 1
while i <= count:
    print(my_list[i])
    i = i + 2

