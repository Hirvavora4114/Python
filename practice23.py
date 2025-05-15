#Search for a number x in this tuple using loop:
tuple=(1,4,9,16,25,36,49,64,81,100)
x=16
idx=0
for el in tuple:
    if(el==x):
        print("number found at idx", idx)
    idx+=1
   
