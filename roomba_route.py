# #This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.
# Ex: Given the following strings...
# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

#starting coords
x = [0,0]
#given string:
route = input("enter route by string of capital letters U D L R that represent directions UP DOWN LEFT RIGHT: ")
print (f"route is: ", route)

#wrtite route, this was googled. list2[i] += 5  first attempt was:  x += [0,1]
for i in route:
    if i == 'U':
        x[1] += 1
    if i == 'D':
        x[1] -= 1
    if i == 'L':
        x[0] -= 1
    if i == 'R':
        x[0] += 1
        
if x != [0,0]:
    print(f"FALSE, DIDNT GET TO START; Final coordinates is: {x}: roomba didn't get to startiong position")
else:
    print (f"TRUE, GOT TO STARTING POSITION; Final coordinates is: {x}, that match starting position")