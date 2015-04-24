#Commands to remember:
##close -- Closes the file. Like File->Save.. in your editor.
##read -- Reads the contents of the file. You can assign the result to a variable.
##readline -- Reads just one line of a text file.
##truncate -- Empties the file. Watch out if you care about the file.
##write('stuff') -- Writes "stuff" to the file.


from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # open tries to be safe by making you explicitly say you want to write a file.

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file." #makes the file and save it in your dir
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

#If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open function and see if that's true.
#Its redundant since, as you noticed, opening in write mode will overwrite the file, more info at Input and Output section of Python documentation.
