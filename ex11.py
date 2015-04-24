print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input() #if your typing in 5'1 you have to type it as 5'1" so it will turn into a triple quote and escape itself to not end the string
print "How much do you weigh?",
weight = raw_input() #you type in your response into the terminal and it saves it as the variable you defined it as.

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


#notes:
#When you typed raw_input() you were typing the ( and ) characters, which are parenthesis characters. This is similar to when you used them to do a format with extra variables, as in "%s %s" % (x, y). For raw_input you can also put in a prompt to show to a person so he knows what to type. Put a string that you want for the prompt inside the () so that it looks like this:

#y = raw_input("Name? ")
#This prompts the user with "Name?" and puts the result into the variable y. This is how you ask someone a question and get the answer.
