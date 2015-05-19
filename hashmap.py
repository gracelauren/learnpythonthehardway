def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key and default (None if not set) when not found.
    """
    bucket  = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v, = kv
        if key == k:
            return i, k, v

    return -1, key, default

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any exisiting value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        #the key exists, replace it
        bucket[i] = (key, value)
    else:
        #the key does not exist, append to create it.
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket: print k, v

# new
# First I start by creating a function that makes a hashmap for you, also known as an initializer. What I've done is created an aMap variable that has a list, and then I put num_buckets lists inside it. These buckets will be used to hold the contents of the hashmap as I set them. Later I use len(aMap) in other functions to find out how many buckets there are. Be sure you understand that!
# hash_key
# This deceptively simple function is the core of how a dict works. What it does is uses the built-in Python hash function to convert a string to a number. Python uses this function for its own dict data structure, and I'm just reusing it. You should fire up a Python console to see how it works. Once I have a number for the key, I then use the % (modulus) operator and the len(aMap) to get a bucket where this key can go. As you should know, the % (modulus) operator will divide any number and give me the remainder. I can also use this as a way of limiting giant numbers to a fixed smaller set of other numbers. If you don't get this then use Python to explore it.
# get_bucket
# This function then uses hash_key to find the bucket that a key could be in. Since I did % len(aMap) in the hash_key function, I know whatever bucket_id I get will fit into the aMap list. Using the bucket_id I can then get the bucket where the key could be.
# get_slot
# This function uses get_bucket to get the bucket a key could be in, and then it simply rolls through every element of that bucket until it finds a matching key. Once it does it returns the tuple of (i, k, v) which is the index the key was found in, the key itself, and the value set for that key. You now know enough to see how this data structure works. It takes keys, hashes and modulus them to find a bucket, then searches that bucket to find the item. This effectively cuts the amount of searching necessary to a fraction of what it would be normally.
# get
# This is a "convenience function" which does what most people want a hashmap to do. It uses get_slot to get the (i, k, v) and then just returns the v (value) only. Make sure you understand how the default variable works, and how the (i, k, v) in get_slot is assigned to the i, k, v variables in get.
# set
# To set a key/value pair all I need to do is get the bucket, and append the new (key, value) to it so it can be found later. However, I want my hashmap to allow one key at a time. To do that, first I have to find the bucket then check if this key already exists. If it does then I replace it in the bucket with the new one, and if it doesn't then I append. This is actually slower than simply appending, but more likely what a user of hashmap wants. If you wanted to allow multiple values for a key you could simply have get go through every slot in the bucket and return a list of everything it found. This is a good example of tradeoffs in design. The current version is faster on get, but slower on set.
# delete
# To delete a key, I simply get the bucket and search for the key in it, and delete it from the list. However, because I chose to make set only store one key/value pair I can stop when I have found one. If I had decided to allow multiple values for each key by simply appending I would have also made delete slower because I would have needed to go through every slot on delete just in case it had a key/value pair that matched.
# list
# The last function is simply a little debug function that prints out what's in the hashmap and should be trivial for you to understand. It just gets each bucket, then goes through each slot in the bucket.



#That means you use a dictionary when:

##You have to retrieve things based on some identifier, like names, addresses, or anything that can be a key.
##You don't need things to be in order. Dictionaries do not normally have any notion of order, so you have to use a list for that.
##You are going to be adding and removing elements and their keys.
