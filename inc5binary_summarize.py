# This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string). 
# Note: neither binary string will contain leading 0s unless the string itself is 0 

# Ex: Given the following binary strings...
# "100" + "1", return "101"
# "11" + "1", return "100"
# "1" + "0", return  "1"

#Time:

x = input("enter first binary string: ")
y = input("enter second binary string: ")

def check_for_correct_input():
    for i in x:
        if x[i] != '1' or '0':
            print(f"string {x} is not a binary string, try again")
            break
    for i in y:
        if y[i] != '1' or '0':
            print(f"string {x} is not a binary string, try again")
            break
    print("input is correct")

def sum_binary_strings():
    check_for_correct_input()
    #had to google binary arithmetic rules
    #reversing strings to operate with
    x = x[::-1]
    y = y[::-1]
    for i in x:
        if x[i] == 1 and y[i] == 1

#need to add track state variable
        
    z = z[::-1]
    print(f"sum is {z}")
    
sum_binary_strings()