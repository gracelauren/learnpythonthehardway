#use argv or raw_input to ask the user what file to open instead of "hard coding" the file's name.

from sys import argv #lines 3-5 uses argv to get a filename

script, filename = argv

txt = open(filename) #run pydoc open and read the instructions. Notice how like your own scripts and raw_input, it takes a parameter and returns a value you can set to your own variable. You just opened a file.

print "Here's your file %r:" % filename #prints a little message
print txt.read() #Here We call a function on txt named read. What you get back from open is a file, and it also has commands you can give it. You give a file a command by using the . (dot or period), the name of the command, and parameters. Just like with open and raw_input. The difference is that txt.read() says, "Hey txt! Do your read command with no parameters!"

print "Type that filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
