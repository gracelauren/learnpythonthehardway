"I am 5'1\" tall."  # escape double-quote inside string
'I am 5\'1" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in." #\t tabs line in
persian_cat = "I'm split\non a line." #\n splits on the line
backslash_cat ="I'm \\ a \\ cat." #\\ puts one slash between words

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
