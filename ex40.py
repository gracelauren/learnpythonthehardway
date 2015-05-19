mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

#Modules are:
##A Python file with some functions or variables in it ..
##You import that file.
##And you can access the functions or variables in that module with the . (dot) operator.

#Common pattern in python:
##Take a key=value style container.
##Get something out of it by the key's name.

#dict style
#get apple from dict
mystuff['apple']

#module style
import mystuff
mystuff.apple() #get apple from the module
mystuff.tangerine #same thing as previous, it's just a variable
print mystuff.tangerine

#class style
#Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
#Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM A CLASSY APPLES!"

thing = MyStuff()
thing.apple()
# print thing.tangerine

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
