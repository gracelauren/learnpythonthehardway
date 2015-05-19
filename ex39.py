#dicts in python are like hashes in ruby, example below:

# >>> things = ['a', 'b', 'c', 'd']
# >>> print things[1]
# b
# >>> things[1] = 'z'
# >>> print things[1]
# z
# >>> things
# ['a', 'z', 'c', 'd']

#What a dict does is let you use anything, not just numbers. Yes, a dict associates one thing to another, no matter what it is.


# >>> stuff = {'name': 'Grace', 'age': 23, 'height': 5 * 12 + 1}
# >>> print stuff['name']
# Grace
# >>> print stuff['age']
# 23
# >>> print stuff['height']
# 61
# >>> stuff['city'] = "Portland"
# >>> print stuff['city']
# Portland

#CAN PUT STUFF IN THE DICTS LIKE THIS:
# >>> stuff[1] = "Wow"
# >>> stuff[2] = "Neato"
# >>> print stuff[1]
# Wow
# >>> print stuff[2]
# Neato
# >>> stuff
# {'city': 'Portland', 2: 'Neato', 'name': 'Grace', 1: 'Wow', 'age': 23, 'height': 61}

#YOU CAN DELETE STUFF WITH THE DEL KEYWORD:
# >>> del stuff['city']
# >>> del stuff[1]
# >>> del stuff[2]
# >>> stuff
# {'name': 'Grace', '23': 39, 'height': 61}

#CREATE A MAPPING OF STATE TO ABBREVIATION
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abberviated %s" % (state, abbrev)

#print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abberviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

#A dictionary is used to map or associate things you want to store to keys you need to get them.              
