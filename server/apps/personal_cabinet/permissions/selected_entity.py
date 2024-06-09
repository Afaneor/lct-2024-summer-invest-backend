import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_selectedentity', always_true)
rules.set_perm('personal_cabinet.add_selectedentity', always_true)
rules.set_perm('personal_cabinet.change_selectedentity', always_true)
rules.set_perm('personal_cabinet.delete_selectedentity', always_true)
rules.set_perm('personal_cabinet.list_selectedentity', always_true)
