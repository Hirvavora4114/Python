info={
    "name":"apnacollege",
    "learning":"coding",
    "subjects":["python","C","Java"],
    "topics":("dict","set"),
    "age": 35,
    "is_adult":True,
    "marks":94.4
}

print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["age"])
#print(info["surname"]) #Error

info["name"]="hirvavora" # Dictionary is mutable
print(info)

null_dict={}
null_dict["name"]="apnacollege"
print(null_dict)
