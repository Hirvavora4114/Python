# Write a program to find the greatest of 4 numbers entered by the user.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=int(input("enter fourth number: "))

if(a>b and a>c and a>d):
    print("first number is the greatest",a)
elif(b>c and b>d):
    print("second number is the greatest",b)
elif(c>d):
    print("third number is the greatest",c)
else:
    print("fourth number is the greatest",d)