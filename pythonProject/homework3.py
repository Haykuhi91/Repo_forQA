'''
1. Use a string concatenation to join the text and print the result.
first_part = “The + operator joins all the”
second_part = “operand strings and returns”
third_part = “a concatenated string.” '''

first_part = "The + operator joins all the"
second_part = "operand strings and returns"
third_part = "a concatenated string."

result = first_part + " " + second_part + " " + third_part
print(result)

'''
2. Get “SDET” characters from the text variable (Hint: use the optional argument of slicing) 
text = "Sally Dolly Ellie Tired"
'''
text = "Sally Dolly Ellie Tired"
new_text = text.split()
print(new_text[0][0]+new_text[1][0] + new_text[2][0] + new_text[3][0])

'''
3. Return the string without any whitespace at the beginning or the end.    
description = "   The method removes any whitespace from the beginning or the end       "
'''
description = "   The method removes any whitespace from the beginning or the end       "

result = description.strip()
print(result)

'''
4. Replace the character “.” with a “!”
method_description = The method replaces a string with another string.
'''
method_description ="The method replaces a string with another string."
print(method_description.replace(".","!"))

'''
5. Write a Python program to calculate the area of a trapezoid (սեղան). Note: A trapezoid is a quadrilateral (քառանկյուն) 
with two sides parallel. An isosceles trapezoid (հավասարասրուն սեղան) is a trapezoid in which the base angles are equal so.
Test data: Height: 5
                   Base, first value: 5
                   Base, second value: 6
                Expected Output: Area is: 27.5

'''
first_base = 5
second_base = 6
height = 5
area = (first_base + second_base)/2 * height
print(area)

'''
6. Find the length of the following strings and print the sentence using formatting.
“The variable A has ___ length, the variable C has ___ length and the variable B has ___ length.”
A = “Geography”
B = “Biology”
C = “Mathematics”

'''
A = "Geography"
B = "Biology"
C = "Mathematics"

length_A = len(A)
length_B = len(B)
length_C = len(C)
text = "The variable A has {} length, the variable C has {} length and the variable B has {} length."
print(text.format(length_A,length_C,length_B))


