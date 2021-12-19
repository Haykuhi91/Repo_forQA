# 1. colors = {“red”, “green”, “blue”}
# a. Add “yellow” in the colors set

colors = {"red", "green", "blue"}

colors.add("yellow")
print(colors)


# b. Add [“purple”, “pink”, “brown”] list to the colors set
colors = {"red", "green", "blue"}
new_colors = {"purple", "pink", "brown"}
colors.update(new_colors)
print(colors)

# c. Remove “blue” from the colors set
colors = {"red", "green", "blue"}
colors.remove("blue")
print(colors)

"""2. Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}"""
# a. Print the value of the "position" key of the Employee dictionary.
Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}

x = Employee["position"]
print(x)

# b. Change the “name” value to “George”.
Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}

Employee["name"] = "George"
print(Employee)

# c. Add “birth_date” : ”18.09.1990” key:value pair to the dictionary.
Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}

Employee.update({"birth_date": "18.09.1990"})
print(Employee)

# d. Remove “surname” from the dictionary.

Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}

Employee.pop("surname")
print(Employee)

# e. Clear the content of the dictionary.
Employee = {
"name": "John",
"surname": "Smith",
"position": "QA Engineer"}

Employee.clear()
print(Employee)