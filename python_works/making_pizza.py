import pizza

# Syntax module_name.function_name()
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Syntax Importing specific functions from a module
# from module_name import function_name or import as manying functions
# from module_name import function_1, function_2
# No need for the dot notation becuz we explicitly imported the function

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Making alias from a function name
# from module_name import function_name as mp
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# Making alias from a module
# import module_name as mn
import pizza as p

# Syntax module_name.function_name()
p.make_pizza(16, 'pepperoni')
p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All functions in a Module
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')