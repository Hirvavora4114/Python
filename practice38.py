#Search if the word "learning" exists in the practice.txt file or not.
word="learning"
with open ("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
        