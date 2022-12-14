''' look at a function that takes a first and last name, and returns a neatly
formatted full name:'''

def formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)
