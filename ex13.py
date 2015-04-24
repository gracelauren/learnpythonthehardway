from sys import argv # An import is how you add features(*his jargon really modules) to your script from the Python feature set.

script, first, second, third = argv #argv is the argument variable; the variable holds the arguments you pass to your Python script when you run it. This line also "unpacks" argv so that it can get assigned to the four diff variables see below to work with

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


#the things that you import to make python program do more are modules


#Run the program like this (and you must pass three command line arguments):

#$ python ex13.py first 2nd 3rd
#the above returns:
    #The script is called: ex13.py
    #Your first variable is: first
    #Your second variable is: 2nd
    #Your third variable is: 3rd



#Remember that modules give you features. Modules. Modules. 
