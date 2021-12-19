#1. colors = [“red”, “green”, “blue”]
#a. Print the second item in the colors list

colors = ["red", "green", "blue"]
print(colors[1])


#b.Change the value from “red” to “yellow” in the colors  list

colors = ["red", "green", "blue"]
colors[0] = "yellow"
print(colors)

#c. Add “brown” to the colors list

colors = ["red", "green", "blue"]
colors.append("brown")
print(colors)

#d.Add “white” as the second item in the colors list

colors = ["red", "green", "blue"]
colors.insert(1,"white")
print(colors)

# e. Remove “blue” from the colors list

colors = ["red", "green", "blue"]
colors.remove("blue")
print(colors)

# f. Use negative indexing to print the last item in the list.

colors = ["red", "green", "blue"]
print(colors[-1])

# g. Use a range of indexes to print the second and third  items in the list.

colors = ["red", "green", "blue"]
print(colors[1:])

# h.Print the number of items in the list.

colors = ["red", "green", "blue"]
print(len(colors))


#2. colors = (“red”, “green”, “blue”)
# a. Print the second item in the colors tuple

colors = ("red", "green", "blue")
print(colors[1])

# b. Use negative indexing to print the last item in the  tuple.

colors = ("red", "green", "blue")
print(colors[-1])

# c. Use a range of indexes to print the second and third  items in the tuple

colors = ("red", "green", "blue")
print(colors[1:])

# d. Print the number of items in the tuple

colors = ("red", "green", "blue")
print(len(colors))


