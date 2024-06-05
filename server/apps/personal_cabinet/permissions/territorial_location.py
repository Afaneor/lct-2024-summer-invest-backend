import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_territoriallocation', always_true)
rules.set_perm('personal_cabinet.add_territoriallocation', always_true)
rules.set_perm('personal_cabinet.change_territoriallocation', always_true)
rules.set_perm('personal_cabinet.delete_territoriallocation', always_true)
rules.set_perm('personal_cabinet.list_territoriallocation', always_true)
