favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

#use list with dictionary in a loop#
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print("*")
        print(f"{name.title()} loves {language} language")
#using keys to check if there is key or not
if "aakash" not in favorite_languages.keys():
    print("AAKASH you are not in team")

#sorting of keys in a loop#
for name in sorted(favorite_languages.keys()):
    print(name)

#use of values() method to print values wighout keys
for name in favorite_languages.values():
    print(name)
#using set() function #
for name in set(favorite_languages.values()):
    print(name)
