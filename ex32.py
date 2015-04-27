# hairs = ['brown', 'blond', 'red'] #heres how to make lists or lists
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]
#Depends on the language and the implementation. In classic terms a list is very different from an array because of how they're implemented. In Ruby though they call these arrays. In Python they call them lists. Just call these lists for now since that's what Python calls them.


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through an list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# NOTE: we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # The range() function only does numbers from the first to the last, not including the last.
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i) #instead of using append we can use use + or +=

#in python range returns a list  so the above can be written like this except if we want it to print each we need a for loop for the printing:
range(0, 6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
