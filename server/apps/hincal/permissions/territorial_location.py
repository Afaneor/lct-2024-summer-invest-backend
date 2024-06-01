import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_territoriallocation', always_true)
rules.set_perm('hincal.add_territoriallocation', always_true)
rules.set_perm('hincal.change_territoriallocation', always_true)
rules.set_perm('hincal.delete_territoriallocation', always_true)
rules.set_perm('hincal.list_territoriallocation', always_true)
