first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(full_name)

# To insert a variable’s value into a string, place the letter f immediately
# before the opening quotation mark.
# These strings are called f-strings. The f is for format, because Python
# formats the string by replacing the name of any variable in braces with its
# value.

#or
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()} !"
print(message)

