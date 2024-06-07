import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_selectionrequest', always_true)
rules.set_perm('personal_cabinet.add_selectionrequest', always_true)
rules.set_perm('personal_cabinet.change_selectionrequest', always_true)
rules.set_perm('personal_cabinet.delete_selectionrequest', always_true)
rules.set_perm('personal_cabinet.list_selectionrequest', always_true)
