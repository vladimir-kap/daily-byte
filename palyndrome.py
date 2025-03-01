x = input("enter a string: ")
y = x[::-1]
z = x[::-1]
def is_string_palyndrome():
    if z == x:
        print(f"you have entered •{x}• given string IS a palyndrome, because reversed string is •{y}•")
    else:
        print(f"you have entered •{x}• given string NOT palyndrome, because reversed string is •{y}•")
        
is_string_palyndrome()