collection=set()
collection.add(1) #adds an element
collection.add(2)
collection.add("apnacollege")
collection.add((1,2,3))
#collection.add([1,2,3,4]) # mutable and unhashable

collection.remove(2) #removes an element
#collection.remove(7) #error
print(collection.pop()) # displays a random 
collection.clear() # empties the set
print(len(collection))
