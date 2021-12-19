'''2. Get “SDET” characters from the text variable (Hint: use the optional argument of slicing)
text = "Sally Dolly Ellie Tired"
'''
text = "Sally Dolly Ellie Tired"

new_text = text.split()

letter = ""
for word in new_text:
    letter = letter + word[0]

print(letter)
