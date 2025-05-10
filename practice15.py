#Write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one.Use subject name as key & marks as value. 
marks={}

x=int(input("enter phy: "))
marks.update({"phy":x})

y=int(input("enter math: "))
marks.update({"math":y})

z=int(input("enter chem: "))
marks.update({"chem":z})

print(marks)