import hashmap

#create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#create a basic set of states and come cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Fransisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

#print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

#do it by using the state then the cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, "Michigan"))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, "Florida"))

#print every state abberviation
print '-' * 10
hashmap.list(states)

#print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

#default values using ||= with the nil result

print "The city for the state 'TX' is: %s" % hashmap.get(cities, 'TX', 'Does not Exist')

#This hashmap is nothing more than "a list of buckets, which are a list of slots, which have key/value pairs in them."
#"a list of buckets..."
##In the hashmap function I create the aMap variable which is a list, and then I fill it with other lists...
#"which are a list of slots..."
##These bucket lists are empty at first, but as we add key/value pairs to the data structure they will fill with "slots" or...
#"which have key/value pairs in them."
##Meaning each slot inside a bucket contains a (key, value) tuple or "pair".


#We'll go through each of these operations using the code, but a general pattern in the hashmap algorithms is this:

##Convert a key to an integer using a hashing function: hash_key.
##Convert this hash to a bucket number using a % (modulus) operator.
##Get this bucket from the aMap list of buckets, and then traverse it to find the slot that contains the key we want.
