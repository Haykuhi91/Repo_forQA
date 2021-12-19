#Exercise 1.
"""Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented by this duration."""

day = int(input("Please enter day value"))
hour = int(input("Please enter hour value"))
minute = int(input("Please enter minute value"))
second = int(input("Please enter second value"))

minutes = 60
hours = 60 * 60
days = 24 * 60 * 60

total_seconds = day * days + hour * hours + minute * minutes + second
print(total_seconds)

#Exercise 2.
"""We consider the three Pythons dictionaries which includes all the computer hardwares:
dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
dicTablet = {"Sumsung": 15, "Other": 13}
Write a Python program that combines by concatenating these three dictionaries into one."""
dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
dicTablet = {"Sumsung": 15, "Other": 13}


dicPC.update({"Sumsung": 22, "Iphone": 9, "Other": 13,"Sumsung": 15, "Other": 13})
print(dicPC)

#Exercise 3.
"""Define a Book class with the following attributes: Title, Author (Full name), Price.
Define a constructor used to initialize the attributes of the method with values entered by the user.
Set the View() method to display information for the current book.
Write a program to testing the Book class."""

class Book:
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Autor = Author
        self.Price = Price
    def View(self):
        print(self.Title, self.Autor, self.Price)

book1 = Book("Jane Eyre","Charlotte Bronte",5000)
book1.View()

#Exercise 4.
"""Write a Python program that create a txt file called myfile.txt and write on it the texte: "Python is object oriented programming language".
Write an other python program that removes the 3rd word from this file."""

f = open("myfile.txt", "w")
f.write("Python is object oriented programming language")
f = open("myfile.txt","w")
f.write("Python is oriented programming language")

#Exercise 5.
"""Two words are anagrams if they contain all of the same letters, but in a different
order. For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that
reads two strings from the user, determines whether or not they are anagrams, and reports the result."""

word1 = input("please enter a word")
word2 = input("please enter a word")

word1_list = list(word1)
word2_list = list(word2)

word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print("Two words are anagrams")
else:
    print("Two words aren't anagrams")








