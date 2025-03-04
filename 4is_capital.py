# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...
# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

#time 3hrs

x = input("enter a string to check for correct use of capitalization: ")

def capitalization():
    capiMock = 0
    if x.isupper():
        print(f"1.CORRECT - given string {x} is uppercase")
    if x.islower():
        print(f"2.CORRECT - given string {x} is lowercase")
    for i in x:
        #used old code from learning py to recall how to use slices in this case
        if x[0].isupper() and x[1:].islower():
            capiMock  = 1
            print(f"3.CORRECT - given string {x} is a name")
            break
    for i in x:
        if not x.isupper() and not x.islower() and capiMock != 1:
            print(f"4.INCORRECT - given string {x} is brokenCase")
            break
#also googled for break usage for printing result only once, and not for every loop iteration
capitalization()