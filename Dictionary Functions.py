student={
    "name":"rahul kumar",
    "subjects": {
        "phy":97,
        "chem":98,
        "math": 95
    }
}

print(len(student)) # displays the length of dictionary
print(list(student.keys())) # returns all keys
print(list(student.values())) # returns all values
pairs=list(student.items()) # returns all (key,val) pairs as tuples
print(pairs[1])
#print(student["name2"]) #error
print(student.get("name2")) #no error -> None (returns the value according to key)
student.update({"city":"delhi"}) #inserts the specified items to the dictionary
print(student)
