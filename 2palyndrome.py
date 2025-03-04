# #facebook job interview question
# This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters. 
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

# Ex: Given the following strings...
# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true

# time: 10 min

x = input("enter a string: ")
y = x[::-1]
z = x[::-1]
def is_string_palyndrome():
    if z == x:
        print(f"you have entered •{x}• given string IS a palyndrome, because reversed string is •{y}•")
    else:
        print(f"you have entered •{x}• given string NOT palyndrome, because reversed string is •{y}•")
        
is_string_palyndrome()