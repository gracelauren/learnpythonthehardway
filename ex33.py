# A while-loop will keep executing the code block under it as long as a boolean expression is True.
#sometimes WHILE loops do not stop so here are some rules to follow:
##Make sure that you use while-loops sparingly. Usually a for-loop is better.
##Review your while statements and make sure that the boolean test will become False at some point.
##When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.


# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d " % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print num


def test_function(i, x, numbers):
    while i < x:
        print "At the top i is %d " % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "The numbers: "
    for num in numbers:
        print num


    # python
    # import ex33
    # ex33.test_function(0,6,[])
