from sys import exit

def wish_room():
    print "This grants you 1-4 wishes. But there might be a consequence for the amount of wishes you make. How many do you ask for? "

    choice = raw_input("> ")
    if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice:
         how_many = int(choice)
    else:
        dead("That's not an option!")

    if how_many >= 0 and how_many <=1:
        print("You are not greedy! You win and are granted three extra wishes with no consequences!")
        exit(0)
    else:
        dead("Uh oh...looks like you half your wishes became the opposite of what you wanted!")

def dead(why):
    print why, "Nice try."
    exit(0)

def start():
    print "You are in a beautiful forest."
    print "You see a tree with an opening near the roots that you can crawl in."
    print "Do you go in? Yes or No"

    choice = raw_input ("> ")

    if choice == "yes" or choice == "Yes" or choice == "YES":
        wish_room()
    elif choice == "no" or choice == "No" or choice == "NO":
        print "Seems like someone lacks a bit of curiosity."
    else:
        dead("You don't know how to follow directions. God smites you and you die.")

start()
