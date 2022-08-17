#This method is used to strip os extra black spaces from start or end
#strip method


#right strip

favorite_language = 'python is a good language.    .   '
favorite_language = favorite_language.rstrip()
print(favorite_language)



#left strip
favorite_language = '      .   python is a good language..'
favorite_language = favorite_language.lstrip()
print(favorite_language)



#from both sides
favorite_language = '   .  python is a good language.    .   '
favorite_language = favorite_language.strip()
print(favorite_language)



