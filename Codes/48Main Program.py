
'''
#module file saved as ModuleOne.py

import ModuleOne
ModuleOne.pizzas("Small","APple","CArrot")
'''

'''
#Importing Specific Functions form Module
#here specific function is imported from Module

from ModuleOne import pizzas
pizzas("Small","APple","CArrot")
'''

'''
#We use function's nickname while importing any function because of name conflict or name size
#here we use shorten function pizzas to p

from ModuleOne import pizzas as p
p("Small","APple","CArrot")
'''

from ModuleOne import pizzas as p
from ModuleOne import cake as c

p("Small","APple","CArrot")
c("Small","APple","CArrot")
