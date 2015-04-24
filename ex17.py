from sys import argv #import imports different methods and other code that already exists
from os.path import exists #exists is a handy command that returns True if the files exists based on its name in a string as an argument

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file).read()
# indata = in_file.read()

print "The input file is %d bytes long" % len(in_file)#changed from indata in the paranthesis to shorten code

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = write(open(to_file, 'w'))
# out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


#notes
#use a simple test file named test.txt:
#$ echo "This is a test file." > test.txt
#$ cat test.txt
##This is a test file.
#$
#$ python ex17.py test.txt new_file.txt
