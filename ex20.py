from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #Each time you do f.seek(0) you're moving to the start of the file. Each time you do f.readline() you're reading a line from the file, and moving the read head to right after the \n that ends that file. 

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Not let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1 #is there a times loop to shorten this?
print_a_line(current_line, current_file)
