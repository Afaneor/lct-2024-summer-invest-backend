import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_selection_request', always_true)
rules.set_perm('personal_cabinet.add_selection_request', always_true)
rules.set_perm('personal_cabinet.change_selection_request', always_true)
rules.set_perm('personal_cabinet.delete_selection_request', always_true)
rules.set_perm('personal_cabinet.list_selection_request', always_true)
