def input_int(min_value, prompt="Please enter a full number", error="Input must be a full number"):
    while True:
        try:
            val_string = input(prompt)
            val_int = int(val_string)
            if val_int >= min_value:
                return val_int
            print(f"Value must be greater tha {min_value}!")
        except ValueError:
            print(error)