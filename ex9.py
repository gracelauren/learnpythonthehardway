days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n is a line break defined as a new line character

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
test
test
test
test
test
test
test
test
test
""" #three double quotes is like an unlimited? varchar

#Notes:
#This \ (backslash) character encodes difficult-to-type characters into a string.
#An important escape sequence is to escape a single-quote ' or double-quote ".
#The second way is by using triple-quotes, which is just """ and works like a string, but you also can put as many lines of text as you want until you type """ again.

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
