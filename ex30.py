# What do you think the if does to the code under it? An if-statement creates what is called a "branch" in the code. It's kind of like those choose your own adventure books where you are asked to turn to one page if you make one choice, and another if you go a different direction. The if-statement tells your script, "If this boolean expression is True, then run the code under it, otherwise skip it."
# Why does the code under the if need to be indented four spaces? A colon at the end of a line is how you tell Python you are going to create a new "block" of code, and then indenting four spaces tells Python what lines of code are in that block. This is exactly the same thing you did when you made functions in the first half of the book.
# What happens if it isn't indented? If it isn't indented, you will most likely create a Python error. Python expects you to indent something after you end a line with a : (colon).
# Can you put other boolean expressions from Exercise 27 in the if-statement? Try it. Yes you can, and they can be as complex as you like, although really complex things generally are bad style.
# What happens if you change the initial values for people, cats, and dogs? Because you are comparing numbers, if you change the numbers, different if-statements will evaluate to True and the blocks of code under them will run. Go back and put different numbers in and see if you can figure out in your head which blocks of code will run.


people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."                            
