from Validation import input_int, y_or_n, input_string, select_item, input_item, valid_g_number


def valid_g_number(n):
    return len(n) == 2 and n[1:2].isdigit()


print(
    input_item("int", "What is your favorite number? ", error="Number must be a whole number, between 0 and 10!", ge=0,
               lt=11))
print(input_item("y_or_n", "Do you have more than one favorite number? (y/n) "))
print(input_item("string", "What is your second favorite number? ",
                 "Number must be 2 characters long, start with 0, and proceed with digits.", valid_g_number))
print(input_item("select",
                 "How did you find your favorite number? A friend or self? ",
                 ["friend", "self"],
                 {
                     "friend": "friend",
                     "self": "self",
                 }))

"""
return len(n) == 9 and n[0] == 'G' and n[1:9].isdigit()
"""

"""
age = input_int("How old are you? ", error="Age must be a whole number, between 0 and 199!", ge=0, lt=120)
print(age)
year = input_int("what year were you born: ", "Must be a year between 1901 and 2024!", gt=1900, le=2024)
print(year)
"""
"""
print(y_or_n("Do you feel you're young? (y/n) "))
"""
"""
print(input_string("What is your name? "))
def valid_g_number(n):
    return len(n) == 9 and n[0] == 'G' and n[1:9].isdigit()
print(input_string("What is your G#? ", "G# must be 9 characters long, start with G, and proceed with digits.", valid=lambda n: len(n) == 9 and n[0] == 'G' and n[1:9].isdigit()))
"""
"""
day = select_item(
    "What day is it?",
    "Must be a day of the week",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    {
            "M": "Monday",
            "Tu": "Tuesday",
            "W": "Wedsnesday",
            "Th": "Thursdsy",
            "F": "Friday",
            "Sat": "Saturday",
            "Sun": "Sunday"
    })
print(day)
print(select_item())
"""
