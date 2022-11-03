# import printing_models
# import printing_models as pm
# from printing_models import print_models, show_completed_models
# from printing_models import print_models as pm, show_completed_models as scm
from printing_models import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
unprinted_copy = unprinted_designs[:]
completed_models = []

print_models(unprinted_copy, completed_models)
print(unprinted_designs)
show_completed_models(completed_models)