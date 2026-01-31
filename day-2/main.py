### Large integers

print(123456789)
print(123_456_789)


### type checking

print(type(123))

### type conversion

print(type(int("123")))
print(type(str(123)))
print(type(float(123)))
print(type(bool("123")))


### operators

print(4 / 2) # implicitly converts the result to float(result: 2.0)
print(4 // 2) # to prevent implicit type conversion (result: 2)
# mathmatical operations priority () > ** > * > / > + > -

### f string

age = 21
name = "John Doe"

print(f"His name is {name} and he is {age} years old")