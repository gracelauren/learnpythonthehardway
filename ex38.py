#How it works:
##Python sees you mentioned mystuff and looks up that variable. It might have to look backward to see if you created with =, if it is a function argument, or if it's a global variable. Either way it has to find the mystuff first.
##Once it finds mystuff it reads the . (period) operator and starts to look at variables that are a part of mystuff. Since mystuff is a list, it knows that mystuff has a bunch of functions.
##It then hits append and compares the name to all the names that mystuff says it owns. If append is in there (it is) then Python grabs that to use.
##Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.
##That extra argument is ... mystuff! I know, weird, right? But that's how Python works so it's best to just remember it and assume that's the result. What happens, at the end of all this, is a function call that looks like: append(mystuff, 'hello') instead of what you read which is mystuff.append('hello').

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1] #first item in list
print stuff [-1] #last item in list like ruby
print stuff.pop() #takes off last item and returns it
print ' '.join(stuff)
print '#'.join(stuff[3:5]) #joins the third and fifth item on a list with a hash imbetween them

#What's a data structure? If you think about it, a "data structure" is just a formal way to structure (organize) some data (facts). It really is that simple, even though some data structures can get insanely complex, all they are is just a way to store facts inside a program so you can access them in different ways. They structure data.
#YOU USE A LIST WHENEVER YOU HAVE SOMETHING THAT MATCHES THE LIST DATA STRUCTURES USEFUL FEATURES:
##If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
##If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
##If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.
