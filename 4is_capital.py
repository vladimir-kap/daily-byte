# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...
# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

x = input("enter a string to check for correct use of capitalization: ")
firstCapi = 0
anyCapi = 0
    
def capitalization():
    for i in x:
        #used old code from learning py to recall how to use slices in this case
        if x[0].isupper() and x[1:].islower():
            firstCapi = 1
    if firstCapi == 1:
        print(f"1.CORRECT - given string: {x} the first letter is {x[0]} and others is lowercase {x[0].isupper()}")
    if x.islower():
        print(f"2.CORRECT - given string {x} is lowercase")
    if x.isupper():
        print(f"3.CORRECT - given string {x} is uppercase")
    for i in x:
        if x[0].isupper() and x[1:].islower():
            if x[1:].isupper():
                anyCapi = 1
    if anyCapi == 1:
        print(f"4.INCORRECT - given string: {x} not a Name or lowercase or uppercase")

    pass

capitalization()