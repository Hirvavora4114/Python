#Write a function to print the elements of a list in a single line.(list is the parameter)
heroes=["thor","ironman","captain america","shaktiman"]

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)