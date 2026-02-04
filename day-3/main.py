### if-else conditions

height = 121

if height == 120:
    print(f"Your height is {height}cm")
else:
    print("Your height is less then 120cm")


number = input('Write a number to check if it is even')
is_even_number =not int(number) % 2 ## not is equivalent to js !


if is_even_number:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


### logical operators(and, or, not)

print(True and True) #True
print(True and False) #False

print(True or False) #True
print(True or True) #True

print(not True) #False
print(not False) #True
