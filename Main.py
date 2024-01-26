from Validation import input_int

age = input_int(0, error="Age must be a whole number!")
print(age)
year = input_int("what year were you born: ", "Must be a year!")
print(year)
test = input_int(error="Heres a string")
print(test)