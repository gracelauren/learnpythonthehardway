#notes
#Functions do three things:
##They name pieces of code the way variables name strings and numbers.
##They take arguments the way your scripts take argv.
##Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."
#create a function by using the word def in Python like JS


# this one is like your scripts with argv
def print_two(*args): #we tell it we want *args (asterisk args) which is a lot like your argv parameter but for functions. This has to go inside () parentheses to work.
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# above is pointless cleaner code below
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zuke","Leela")
print_two_again("Zuke","Leela")
print_one("First!")
print_none()
